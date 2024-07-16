from fastapi import Depends

from app.configs import BaseCrud
from app.helpers.get_current_user import get_current_user
from app.models.professionals import Professional
from app.schemas.input_schemas import DefaultPagination
from app.schemas.professional_schemas import PaginatedProfessionalsSchema as PPS


async def get_all(
    query_params: DefaultPagination = Depends(),
    current_user: str = Depends(get_current_user),
) -> PPS:
    """Get all professionals"""
    professionals, count, pages = await BaseCrud(Professional).paginate_records(
        query_params
    )
    return PPS(
        data=professionals,
        current_page=query_params.page,
        total_pages=pages,
        total_records=count,
    )
