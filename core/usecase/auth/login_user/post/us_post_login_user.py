from rest_framework.response import Response
from django.contrib.auth.models import User
from modules.module_auth.orm.model.user.requests.request_login import RequestLogin
from modules.module_auth.orm.model.token.requests.request_generate_token import RequestGenerateToken
from django.contrib.auth import login

class UsPostLoginUser:
	def execute(request):
		try:
			user = RequestLogin.execute(username=request.data.get('username'), password=request.data.get('password'))
			if user is not None:
				login(request, user)
			token = RequestGenerateToken.execute(user=user)
		except User.DoesNotExist:
			return Response({'response': 'Неверные логин или пароль'})

		return Response({
			'response': 'Вы успешно вошли в аккаунт',
			'token': token
		})
