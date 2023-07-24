from rest_framework.views import APIView
from layers.Interactor.usecase.login_user.post.us_post_login_user import us_post_login_user
from rest_framework.authentication import TokenAuthentication
from layers.CustomPermission.IsNotAuthenticated import IsNotAuthenticated

class RouteLoginUser(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsNotAuthenticated]

    def post(self, request):
        return us_post_login_user.execute(request)