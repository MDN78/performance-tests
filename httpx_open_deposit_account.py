import time
import httpx

# Данные для создания пользователя
create_user_payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

# Выполняем запрос на создание пользователя
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
assert create_user_response.status_code == httpx.codes.OK
create_user_response_data = create_user_response.json()
create_user_id = create_user_response_data['user']['id']

# Выполняем запрос на открытие депозитного счета пользователя по ID
user_payload = {
    "userId": create_user_id
}

open_user_deposit_account = httpx.post(
    "http://localhost:8003/api/v1/accounts/open-deposit-account", json=user_payload
)

# Выводим полученные данные - статус код и json ответ сервера
print("User deposit response:", open_user_deposit_account.json())
print("Status Code:", open_user_deposit_account.status_code)
