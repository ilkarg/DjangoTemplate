from rest_framework.response import Response
from layers.ORM.model.News.NewsController import NewsController
from layers.ORM.model.News.NewsSerializer import NewsSerializer

class us_get_load_all_news:
	def execute(request):
		return Response(NewsController.load_all_news())
