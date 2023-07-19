from rest_framework.response import Response
from layers.ORM.model.News.News import News
from layers.ORM.model.News.NewsSerializer import NewsSerializer

class us_get_load_all_news:
	def execute(request):
		return Response(News.objects.values())