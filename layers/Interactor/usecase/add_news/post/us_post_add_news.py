from rest_framework.response import Response
from layers.ORM.model.News.NewsController import NewsController
from layers.ORM.model.News.NewsSerializer import NewsSerializer

class us_post_add_news:
    def execute(request):
        news = NewsController.create_news(title=request.data.get('title'), body=request.data.get('body'))
        news_serialized = NewsSerializer(news)
        return Response({'title': news_serialized.data['title'], 'body': news_serialized.data['body']})
