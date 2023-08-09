from rest_framework.response import Response
from layers.ORM.model.Token.TokenController import TokenController
from rest_framework.authtoken.models import Token

class us_post_logout_user:
    def execute(request):
        status = TokenController.remove_token(user=request.user)
        if status:
            return Response({'response': 'Вы успешно вышли из аккаунта'})
        else:
            return Response({'response': 'Во время выхода из аккаунта, что-то пошло не так'})
