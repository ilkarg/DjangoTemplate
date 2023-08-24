from rest_framework.response import Response
from modules.module_news.orm.model.news.requests.request_load_news import RequestLoadNews
from modules.module_news.orm.model.news.news_serializer import NewsSerializer

class UsGetLoadNews:
	def execute(request, id):
		news = RequestLoadNews.execute(id=id)
		return Response({'title': news.title, 'body': news.body})
