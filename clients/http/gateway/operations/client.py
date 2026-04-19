from typing import TypedDict
from httpx import Response, QueryParams

from clients.http.client import HTTPClient


class GetOperationsQueryDict(TypedDict):
    """
    Структура данных для получения списка операций пользователя.
    """
    accountId: str


class GetOperationsSummaryQueryDict(TypedDict):
    """
    Структура данных для получения статистики операций пользователя.
    """
    accountId: str


class MakeOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции комиссии
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeTopUpOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции пополнения
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeCashbackOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции кэшбэка
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeTransferOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции трансфера
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции покупки
    """
    category: str


class MakeBillPaymentOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции оплаты по счету
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeCashWithdrawalOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции снятия наличных денег
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class OperationsGatewayHTTPClient(HTTPClient):

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получение информации об операции по operation_id
        :param operation_id: идентификатор операции
        :return: Ответ от сервера (объект httpx.Response)
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получение чека по операции по operation_id
        :param operation_id:  operation_id: идентификатор операции
        :return: Ответ от сервера (объект httpx.Response)
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Получение списка операций для определенного счета
        :param query: accountId
        :return: Ответ от сервера (объект httpx.Response)
        """
        return self.get("/api/v1/operations", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        Получение статистики по операциям для определенного счета
        :param query: accountId
        :return: Ответ от сервера (объект httpx.Response)
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query))

    def make_fee_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создание операции комиссии
        :param request: словарь с данными операции
        :return: Ответ от сервера (объект httpx.Response)
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Создание операции пополнения
        :param request: словарь с данными операции
        :return: Ответ от сервера (объект httpx.Response)
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        Создание операции кэшбэка
        :param request: словарь с данными операции
        :return: Ответ от сервера (объект httpx.Response)
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Создание операции перевода
        :param request: словарь с данными операции
        :return: Ответ от сервера (объект httpx.Response)
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Создание операции покупки
        :param request: словарь с данными операции
        :return: Ответ от сервера (объект httpx.Response)
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Создание операции оплаты по счету
        :param request: словарь с данными операции
        :return: Ответ от сервера (объект httpx.Response)
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        Создание операции снятия наличных денег
        :param request: словарь с данными операции
        :return: Ответ от сервера (объект httpx.Response)
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)
