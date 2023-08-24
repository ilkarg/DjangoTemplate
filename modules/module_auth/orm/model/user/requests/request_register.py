from django.contrib.auth.models import User

class RequestRegister:
    def execute(username, password):
        user = User(username=request.data.get('username'), password=request.data.get('password'))
        user.is_staff = True
        user.save()
        return user
