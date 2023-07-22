from rest_framework.views import APIView
from layers.Interactor.usecase.login_user.post.us_post_login_user import us_post_login_user

class RouteLoginUser(APIView):
    def post(self, request):
    	return us_post_login_user.execute(request)