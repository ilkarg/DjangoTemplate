from rest_framework.authtoken.models import Token

class RequestGenerateToken:
    def execute(user):
        token = Token.objects.get_or_create(user=user)[0].key
        return token
