from rest_framework.response import Response
from rest_framework.authtoken.models import Token

class us_post_logout_user:
    def execute(request):
      token = Token.objects.get(user=request.user)
      token.delete()
      return Response({'response': 'Вы успешно вышли из аккаунта'})