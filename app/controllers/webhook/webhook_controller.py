from app.configs.base_crud import BaseCrud
from app.models.users import User
from app.services.messages_wpp_services import MessagesWppServices


async def answer_message(session_token: str, data: dict) -> bool:
    """This will receive a webhook from wppconnect and process the message received."""
    if data["event"] == "onmessage" and data["isGroupMsg"] == False:
        print(session_token)
        current_user = await BaseCrud(User).get_record(
            filters=[User.session_token == session_token], unique=True
        )
        if current_user.is_active:
            print(data["from"].split("@")[0], data["content"])
            await MessagesWppServices(current_user).answer(
                data["from"].split("@")[0], data["content"]
            )

    return True
