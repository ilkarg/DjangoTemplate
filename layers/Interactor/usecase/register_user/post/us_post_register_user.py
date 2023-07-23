from rest_framework.response import Response
from django.contrib.auth.models import User

class us_post_register_user:
    def execute(request):
    	user = User(username=request.data.get('login'), email=request.data.get('email'), password=request.data.get('password'))
    	user.is_staff = True
    	user.save()
    	return Response({'response': 'Аккаунт успешно зарегистрирован!'})