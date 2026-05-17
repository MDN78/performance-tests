import grpc
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import UsersGatewayServiceStub
from contracts.services.gateway.users.rpc_get_user_pb2 import GetUserRequest


# пример Перехватчик вызовов, позволяющий обрабатывать или модифицировать gRPC-запросы и ответы

class SimpleLoggingInterceptor(grpc.UnaryUnaryClientInterceptor):
    def intercept_unary_unary(self, continuation, client_call_details, request):
        # Печатаем имя вызываемого метода
        print(f"[gRPC Interceptor] Calling method: {client_call_details.method}")

        # Выполняем реальный RPC вызов
        response = continuation(client_call_details, request)

        return response


channel = grpc.insecure_channel("localhost:9003")
intercept_channel = grpc.intercept_channel(channel, SimpleLoggingInterceptor())

stub = UsersGatewayServiceStub(intercept_channel)

request = GetUserRequest(id="0ba6144f-3db4-4c7b-bedc-6e64fa39a8e8")
response = stub.GetUser(request)

print(response)
