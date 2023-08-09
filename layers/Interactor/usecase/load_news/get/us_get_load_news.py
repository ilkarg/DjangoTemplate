from rest_framework.response import Response
from layers.ORM.model.News.NewsController import NewsController
from layers.ORM.model.News.NewsSerializer import NewsSerializer

class us_get_load_news:
	def execute(request, id):
		news = NewsController.load_news(id=id)
		return Response({'title': news.title, 'body': news.body})
