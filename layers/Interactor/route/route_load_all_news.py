from rest_framework.views import APIView
from layers.Interactor.usecase.load_all_news.get.us_get_load_all_news import us_get_load_all_news

class RouteLoadAllNews(APIView):
    def get(self, request):
        return us_get_load_all_news.execute(request)