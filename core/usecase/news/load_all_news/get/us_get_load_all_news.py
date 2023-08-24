from rest_framework.response import Response
from modules.module_news.orm.model.news.requests.request_load_all_news import RequestLoadAllNews
from modules.module_news.orm.model.news.news_serializer import NewsSerializer

class UsGetLoadAllNews:
	def execute(request):
		return Response(RequestLoadAllNews.execute())
