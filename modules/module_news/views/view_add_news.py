from rest_framework.views import APIView
from core.usecase.news.add_news.post.us_post_add_news import UsPostAddNews

class ViewAddNews(APIView):
    def post(self, request):
        return UsPostAddNews.execute(request)
