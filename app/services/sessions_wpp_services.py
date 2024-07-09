import time

import requests

from app.configs.base_crud import BaseCrud
from app.configs.settings import settings
from app.models.users import User
from app.services.base_wpp_services import BaseWppService

SECURE_TOKEN = settings.secure_token


class SessionWppService(BaseWppService):
    def __init__(self, current_user):
        super().__init__(current_user)

    async def generate_token(self) -> str:
        """Generate token for user"""
        response = requests.post(f"{self.api_url}/{SECURE_TOKEN}/generate-token")

        if response.status_code != 201:
            raise Exception("Error on generate token")

        await BaseCrud(User).update_record(
            instance_id=self.current_user.id,
            data={"session_token": response.json()["token"]},
        )
        return response.json()["token"]

    async def get_qrcode(self) -> bytes:
        """Get qrcode from wppconnect"""
        requests.post(
            f"{self.api_url}/start-session",
            headers=self.headers,
            json={
                "webhook": f"http://api:8000/api/v1/answer/{self.current_user.session_token}"
            },
        )

        for _ in range(3):
            qrcode_response = requests.get(
                f"{self.api_url}/qrcode-session", headers=self.headers
            )
            if type(qrcode_response.content) == bytes:
                return qrcode_response.content

            time.sleep(1)

    async def get_status(self) -> dict:
        """Get status from wppconnect"""
        response = requests.get(f"{self.api_url}/status-session", headers=self.headers)

        return response.json()

    async def close_session(self) -> None:
        """Close the session and logout from the whatsapp"""
        response = requests.post(f"{self.api_url}/logout-session", headers=self.headers)
        BaseCrud(User).update_record(
            instance_id=self.current_user.id,
            data={"session_token": None},
        )
        return response.json()

    async def stop_session(self) -> None:
        """Stop the session for don't receive messages anymore"""
        response = requests.post(f"{self.api_url}/stop-session", headers=self.headers)
        BaseCrud(User).update_record(
            instance_id=self.current_user.id,
            data={"session_token": None},
        )
        return response.json()
