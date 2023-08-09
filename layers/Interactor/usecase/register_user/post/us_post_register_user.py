from rest_framework.response import Response
from layers.ORM.model.User.UserController import UserController

class us_post_register_user:
    def execute(request):
        user = UserController.register(username=request.data.get('username'), password=request.data.get('password'))
    	return Response({'response': 'Аккаунт успешно зарегистрирован!'})
