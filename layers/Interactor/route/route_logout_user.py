from rest_framework.views import APIView
from layers.Interactor.usecase.logout_user.post.us_post_logout_user import us_post_logout_user
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class RouteLogoutUser(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
      return us_post_logout_user.execute(request)