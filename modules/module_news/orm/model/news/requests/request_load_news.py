from modules.module_news.orm.model.news.news import News

class RequestLoadNews:
    def execute(id):
        news = News.objects.get(id=id)
        return news
