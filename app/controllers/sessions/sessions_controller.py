from fastapi import Depends, Response

import app.schemas.session_schemas as output
from app.helpers.get_current_user import get_current_user
from app.services.sessions_wpp_services import SessionWppService


async def connect_qrcode(current_user: str = Depends(get_current_user)) -> bytes:
    """Get the qrcode from wppconnect and return it to the user"""
    await SessionWppService(current_user).generate_token()
    qrcode_response = await SessionWppService(current_user).get_qrcode()

    return Response(content=qrcode_response, media_type="image/png")


async def close_session(current_user: str = Depends(get_current_user)):
    """Close the session and logout from the whatsapp"""
    response = await SessionWppService(current_user).close_session()

    return response


async def status_session(current_user: str = Depends(get_current_user)):
    """Get the status of the session"""
    status_response = await SessionWppService(current_user).get_status()
    return status_response
