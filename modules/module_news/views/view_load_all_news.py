from rest_framework.views import APIView
from core.usecase.news.load_all_news.get.us_get_load_all_news import UsGetLoadAllNews
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class ViewLoadAllNews(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return UsGetLoadAllNews.execute(request)
