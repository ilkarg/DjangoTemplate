from rest_framework.response import Response
from modules.module_auth.orm.model.token.requests.request_remove_token import RequestRemoveToken
from rest_framework.authtoken.models import Token

class UsPostLogoutUser:
    def execute(request):
        status = RequestRemoveToken.execute(user=request.user)
        if status:
            return Response({'response': 'Вы успешно вышли из аккаунта'})
        else:
            return Response({'response': 'Во время выхода из аккаунта, что-то пошло не так'})
