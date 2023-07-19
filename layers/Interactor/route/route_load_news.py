from rest_framework.views import APIView
from layers.Interactor.usecase.load_news.get.us_get_load_news import us_get_load_news

class RouteLoadNews(APIView):
    def get(self, request):
        return us_get_load_news.execute(request)