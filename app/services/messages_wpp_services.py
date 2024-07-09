import requests
from sqlalchemy import asc

from app.configs.base_crud import BaseCrud
from app.external.gpt import GPT
from app.models.users import User
from app.services.base_wpp_services import BaseWppService


class MessagesWppServices(BaseWppService):
    def __init__(self, current_user: User):
        super().__init__(current_user)

    async def answer(self, phone: str, message: str):
        """Answer the message received"""
        await BaseCrud(Message).create_record(
            {"role": "user", "content": message, "user_id": self.current_user.id, "phone": phone}
        )
        last_messages_by_phone = await self._get_last_messages(phone)
        gpt_answer = await GPT().get_gpt_answer(last_messages_by_phone)
        await BaseCrud(Message).create_record(
            {"role": "system", "content": gpt_answer, "user_id": self.current_user.id, "phone": phone}
        )

        requests.post(
            f"{self.api_url}/send-message",
            headers=self.headers,
            json={"phone": phone, "isGroup": False, "isNewsletter": False, "message": gpt_answer},
        )

        return True

    async def _get_last_messages(self, phone: str):
        messages = await BaseCrud(Message).search_records(
            filters=[Message.user_id == self.current_user.id, Message.phone == phone],
            order_by=[Message.created_at.asc()],
        )
        gpt_messages = [{"role": "system", "content": self.current_user.prompt}]
        for message in messages:
            gpt_messages.append(
                {
                    "role": message.role,
                    "content": message.content,
                }
            )
            print(message.content)
        return gpt_messages
