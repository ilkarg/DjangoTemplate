from rest_framework.views import APIView
from core.usecase.auth.register_user.post.us_post_register_user import UsPostRegisterUser
from rest_framework.authentication import TokenAuthentication
from core.custom_permission.is_not_authenticated import IsNotAuthenticated

class ViewRegisterUser(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsNotAuthenticated]

    def post(self, request):
        return UsPostRegisterUser.execute(request)
