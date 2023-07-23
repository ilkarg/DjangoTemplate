from rest_framework.views import APIView
from layers.Interactor.usecase.login_user.post.us_post_login_user import us_post_login_user
from rest_framework.permissions import AllowAny

class RouteLoginUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
    	return us_post_login_user.execute(request)