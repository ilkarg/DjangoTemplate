from rest_framework.views import APIView
from core.usecase.auth.logout_user.post.us_post_logout_user import UsPostLogoutUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class ViewLogoutUser(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        return UsPostLogoutUser.execute(request)
