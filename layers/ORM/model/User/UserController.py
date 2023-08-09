from django.contrib.auth.models import User

class UserController:
    def login(username, password):
        user = User.objects.get(username=username, password=password)
        return user

    def register(username, password):
        user = User(username=request.data.get('username'), password=request.data.get('password'))
    	user.is_staff = True
    	user.save()
        return user
