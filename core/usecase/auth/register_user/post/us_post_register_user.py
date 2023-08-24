from rest_framework.response import Response
from modules.module_auth.orm.model.user.requests.request_register import RequestRegister

class UsPostRegisterUser:
    def execute(request):
        user = RequestRegister.execute(username=request.data.get('username'), password=request.data.get('password'))
        return Response({'response': 'Аккаунт успешно зарегистрирован!'})
