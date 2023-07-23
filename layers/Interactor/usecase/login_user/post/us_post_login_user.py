from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import login

class us_post_login_user:
	def execute(request):
		try:
			user = User.objects.get(username=request.data.get('username'), password=request.data.get('password'))
			if user is not None:
				login(request, user)
			token = Token.objects.get_or_create(user=user)[0].key
		except User.DoesNotExist:
			return Response({'response': 'Неверные логин или пароль'})

		return Response({
			'response': 'Вы успешно вошли в аккаунт',
			'token': token
		})