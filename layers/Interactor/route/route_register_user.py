from rest_framework.views import APIView
from layers.Interactor.usecase.register_user.post.us_post_register_user import us_post_register_user
from rest_framework.permissions import AllowAny

class RouteRegisterUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
    	return us_post_register_user.execute(request)