from fastapi import Depends

from app.configs import BaseCrud
from app.helpers.get_current_user import get_current_user
from app.models.appointments import Appointment
from app.schemas.appointment_schemas import PaginatedAppointmentsSchema as PAS
from app.schemas.input_schemas import DefaultPagination


async def get_all(
    query_params: DefaultPagination = Depends(),
    current_user: str = Depends(get_current_user),
) -> PAS:
    """Get all appointments"""
    appointments, count, pages = await BaseCrud(Appointment).paginate_records(
        query_params
    )
    return PAS(
        data=appointments,
        current_page=query_params.page,
        total_pages=pages,
        total_records=count,
    )
