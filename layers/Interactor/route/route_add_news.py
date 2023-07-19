from rest_framework.views import APIView
from layers.Interactor.usecase.add_news.post.us_post_add_news import us_post_add_news

class RouteAddNews(APIView):
    def post(self, request):
        return us_post_add_news.execute(request)