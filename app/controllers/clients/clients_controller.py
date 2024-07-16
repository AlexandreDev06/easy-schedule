from fastapi import Depends

from app.configs import BaseCrud
from app.helpers.get_current_user import get_current_user
from app.models.clients import Client
from app.models.users import User
from app.schemas.client_schemas import PaginatedClientsSchema
from app.schemas.input_schemas import DefaultPagination


async def get_all(
    query_params: DefaultPagination = Depends(),
    current_user: User = Depends(get_current_user),
) -> PaginatedClientsSchema:
    """Get all clients"""
    clients, count, pages = await BaseCrud(Client).paginate_records(query_params)
    return PaginatedClientsSchema(
        data=clients,
        current_page=query_params.page,
        total_pages=pages,
        total_records=count,
    )
