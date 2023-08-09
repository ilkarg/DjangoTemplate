from rest_framework.response import Response
from django.contrib.auth.models import User
from layers.ORM.model.User.UserController import UserController
from layers.ORM.model.Token.TokenController import TokenController
from django.contrib.auth import login

class us_post_login_user:
	def execute(request):
		try:
			user = UserController.login(username=request.data.get('username'), password=request.data.get('password'))
			if user is not None:
				login(request, user)
			token = TokenController.generate_token(user=user)
		except User.DoesNotExist:
			return Response({'response': 'Неверные логин или пароль'})

		return Response({
			'response': 'Вы успешно вошли в аккаунт',
			'token': token
		})
