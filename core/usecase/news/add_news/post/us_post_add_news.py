from rest_framework.response import Response
from modules.module_news.orm.model.news.requests.request_create_news import RequestCreateNews
from modules.module_news.orm.model.news.news_serializer import NewsSerializer

class UsPostAddNews:
    def execute(request):
        news = RequestCreateNews.execute(title=request.data.get('title'), body=request.data.get('body'))
        news_serialized = NewsSerializer(news)
        return Response({'title': news_serialized.data['title'], 'body': news_serialized.data['body']})
