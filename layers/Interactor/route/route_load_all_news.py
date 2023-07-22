from rest_framework.views import APIView
from layers.Interactor.usecase.load_all_news.get.us_get_load_all_news import us_get_load_all_news
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class RouteLoadAllNews(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return us_get_load_all_news.execute(request)