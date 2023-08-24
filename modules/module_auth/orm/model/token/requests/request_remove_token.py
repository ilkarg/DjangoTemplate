from rest_framework.authtoken.models import Token

class RequestRemoveToken:
    def execute(user):
        token = Token.objects.get(user=user)
        token.delete()
        return True
