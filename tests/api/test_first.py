import pytest


@pytest.mark.smoke
def test_check_status_get_users(users_client, user_data):
    resp = users_client.get_users()
    resp.check_status(200)


@pytest.mark.smoke
def test_create_users(users_client, user_data):
    resp_2 = users_client.create_user(user_data)
    data = {"id": user_data.id, "userName": user_data.userName, "password": user_data.password}
    resp_2.exact_body(data)


@pytest.mark.smoke
def test_negative(users_client, user_data):
    resp_2 = users_client.create_user(user_data)
    data = {"id": user_data.userName, "userName": user_data.userName, "password": user_data.password}
    resp_2.exact_body(data)
