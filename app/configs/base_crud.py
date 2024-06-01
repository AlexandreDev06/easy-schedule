import math

from sqlalchemy import delete, func, select, update
from sqlalchemy.orm import DeclarativeBase, joinedload
from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy.orm.strategy_options import Load
from sqlalchemy.sql.elements import BinaryExpression

from app.configs.database import DBConnection


class BaseCrud:
    def __init__(self, model: DeclarativeBase = None) -> None:
        self.model = model

    async def get_record(
        self,
        instance_id: int = None,
        filters: list[BinaryExpression] = None,
        options: list[BinaryExpression] = None,
        join: list[DeclarativeBase] = None,
        unique: bool = False,
    ):
        query = select(self.model)

        if instance_id:
            query = query.filter(self.model.id == instance_id)
            unique = True

        if join:
            for model in join:
                query = query.options(joinedload(model))

        if filters:
            query = query.filter(*filters)

        if options:
            query = query.options(*options)

        with DBConnection() as conn:
            query = conn.session.scalars(query)
            if unique:
                return query.unique().first()

            return query

    async def update_record(
        self,
        instance_id: int,
        data: dict,
    ) -> None:
        with DBConnection() as conn:
            try:
                conn.session.execute(
                    update(self.model)
                    .where(self.model.id == instance_id)
                    .values(**data)
                    .execution_options(synchronize_session="fetch")
                )
                conn.session.commit()
            except Exception as exe:
                conn.session.rollback()
                print(exe)

    async def create_record(self, data: dict) -> None:
        with DBConnection() as conn:
            try:
                new_instance = self.model(**data)
                conn.session.add(new_instance)
                conn.session.commit()
                conn.session.refresh(new_instance)
                return new_instance
            except Exception as exe:
                conn.session.rollback()
                print(exe)

    async def delete_record(
        self,
        instance_id: int = None,
        filters: list[BinaryExpression] = None,
        instance: DeclarativeBase = None,
    ) -> bool:
        query = select(self.model)

        if instance_id:
            query = query.filter(self.model.id == instance_id)

        if filters:
            query = query.filter(*filters)

        with DBConnection() as conn:
            try:
                result = instance
                if not instance:
                    query = conn.session.scalars(query)
                    result = query.unique().first()

                if result:
                    query = delete(self.model).where(self.model.id == result.id)
                    conn.session.execute(query)
                    conn.session.commit()
                    return True
            except Exception as exe:
                print(exe)
                conn.session.rollback()

        return False

    async def search_records(
        self,
        filters: list[BinaryExpression] = None,
        offset: int = None,
        limit: int = None,
        order_by: list[InstrumentedAttribute] = None,
        options: list[Load] = None,
        join: list[DeclarativeBase] = None,
        only_count: bool = False,
    ):
        query = select(self.model)

        if only_count:
            query = select(func.count()).select_from(self.model)

        if options:
            query = query.options(*options)

        if filters:
            query = query.filter(*filters)

        if order_by:
            query = query.order_by(*order_by)

        if offset and not only_count:
            query = query.offset(offset)

        if limit and not only_count:
            query = query.limit(limit)

        if join:
            for model in join:
                query = query.options(joinedload(model))

        with DBConnection() as conn:
            query = conn.session.execute(query)

            if only_count:
                count = query.scalar_one()
                pages = await self._calculate_pages(count, limit) if limit else None
                return count, pages

            return query.scalars().all()

    async def _calculate_pages(self, query_count: int, limit: int) -> int:
        total_pages = math.ceil(query_count / limit)
        return 1 if total_pages <= 0 else total_pages

    async def _calculate_offset(self, page: int, limit: int) -> int:
        # page always starts at 1, offset always starts at 0
        return (page - 1) * limit
