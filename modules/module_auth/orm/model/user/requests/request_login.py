from django.contrib.auth.models import User

class RequestLogin:
    def execute(username, password):
        user = User.objects.get(username=username, password=password)
        return user
