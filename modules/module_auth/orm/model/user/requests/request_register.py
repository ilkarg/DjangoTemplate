from django.contrib.auth.models import User

class RequestRegister:
    def execute(username, password):
        user = User(username=username, password=password)
        user.is_staff = True
        user.save()
        return user
