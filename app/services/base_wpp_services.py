from app.configs.settings import settings

SECURE_TOKEN = settings.secure_token


class BaseWppService:
    def __init__(self, current_user):
        self.current_user = current_user
        self.api_url = f"http://wppconnect-server:21465/api/{current_user.id}"
        self.headers = {"Authorization": f"Bearer {current_user.session_token}"}
