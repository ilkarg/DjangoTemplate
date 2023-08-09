class TokenController:
    def generate_token(user):
        token = Token.objects.get_or_create(user=user)[0].key
        return token

    def remove_token(user):
        token = Token.objects.get(user=user)
        token.delete()
        return true
