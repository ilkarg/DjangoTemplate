from rest_framework.views import APIView
from core.usecase.news.load_news.get.us_get_load_news import UsGetLoadNews

class ViewLoadNews(APIView):
    def get(self, request, id):
        return UsGetLoadNews.execute(request, id)
