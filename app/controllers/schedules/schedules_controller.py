from fastapi import Depends

from app.configs import BaseCrud
from app.helpers.get_current_user import get_current_user
from app.models.schedules import Schedule
from app.schemas.input_schemas import DefaultPagination
from app.schemas.schedule_schemas import PaginatedSchedulesSchema as PSS
from app.schemas.schedule_schemas import PostScheduleSchema


async def get_all(
    query_params: DefaultPagination = Depends(),
    current_user: str = Depends(get_current_user),
) -> PSS:
    """Get all schedules"""
    schedules, count, pages = await BaseCrud(Schedule).paginate_records(query_params)
    return PSS(
        data=schedules,
        current_page=query_params.page,
        total_pages=pages,
        total_records=count,
    )

async def create(
    schedule: PostScheduleSchema,
    current_user: str = Depends(get_current_user),
) -> PostScheduleSchema:
    """Create a new Schedule"""
    return await BaseCrud(Schedule).create_record(schedule.__dict__)
