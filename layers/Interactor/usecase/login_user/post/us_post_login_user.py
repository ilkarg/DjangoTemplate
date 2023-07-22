from rest_framework.response import Response
from django.contrib.auth.models import User

class us_post_login_user:
    def execute(request):
    	try:
    		user = User.objects.get(username=request.data.get('login'), password=request.data.get('password'))
    	except User.DoesNotExist:
    		return Response({'message': 'Неверные логин или пароль'})

    	return Response({'message': 'Вы успешно вошли в аккаунт'})