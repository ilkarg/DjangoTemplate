from rest_framework.views import APIView
from layers.Interactor.usecase.register_user.post.us_post_register_user import us_post_register_user
from rest_framework.authentication import TokenAuthentication
from layers.CustomPermission.IsNotAuthenticated import IsNotAuthenticated

class RouteRegisterUser(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsNotAuthenticated]

    def post(self, request):
        return us_post_register_user.execute(request)