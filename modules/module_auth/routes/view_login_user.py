from rest_framework.views import APIView
from core.usecase.auth.login_user.post.us_post_login_user import UsPostLoginUser
from rest_framework.authentication import TokenAuthentication
from core.custom_permission.is_not_authenticated import IsNotAuthenticated

class ViewLoginUser(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsNotAuthenticated]

    def post(self, request):
        return UsPostLoginUser.execute(request)
