import allure

from core.client import ApiClient


class UsersClient(ApiClient):
    def __init__(self, url):
        self.api_client = ApiClient(url)

    @allure.step
    def get_users(self):
        return self.api_client.get("/api/v1/Users")

    @allure.step
    def create_user(self, user_data):
        data = {"id": user_data.id, "userName": user_data.userName, "password": user_data.password}
        return self.api_client.post("/api/v1/Users", body=data)
