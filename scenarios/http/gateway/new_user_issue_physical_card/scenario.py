from locust import task

from clients.http.gateway.accounts.schema import OpenDebitCardAccountResponseSchema
from clients.http.gateway.locust import GatewayHTTPSequentialTaskSet
from clients.http.gateway.users.schema import CreateUserResponseSchema
from tools.locust.user import LocustBaseUser


class IssuePhysicalCardSequentialTaskSet(GatewayHTTPSequentialTaskSet):
    """
    Класс сценария: описывает последовательный флоу нового пользователя по выпуску физической карты
    """
    create_user_response: CreateUserResponseSchema | None = None
    open_open_debit_card_account_response: OpenDebitCardAccountResponseSchema | None = None

    @task
    def create_user(self):
        # Создаем нового пользователя
        self.create_user_response = self.users_gateway_client.create_user()

    @task
    def open_debit_card_account(self):
        if not self.create_user_response:
            return
        # Открываем дебетовый счёт для нового пользователя
        self.open_open_debit_card_account_response = self.accounts_gateway_client.open_debit_card_account(
            user_id=self.create_user_response.user.id
        )

    @task
    def issue_physical_card(self):
        if not self.open_open_debit_card_account_response:
            return
        # Выпускаем физическую карту к открытому дебетовому счету для нового пользователя
        self.cards_gateway_client.issue_physical_card(
            user_id=self.create_user_response.user.id,
            account_id=self.open_open_debit_card_account_response.account.id
        )


class IssuePhysicalCardScenarioUser(LocustBaseUser):
    tasks = [IssuePhysicalCardSequentialTaskSet]
