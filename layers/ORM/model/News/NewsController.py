from layers.ORM.model.News.News import News

class NewsController:
    def create_news(title, body):
        news = News(title=title, body=body)
        news.save()
        return news

    def load_all_news():
        return News.objects.values()

    def load_news(id):
        news = News.objects.get(id=id)
        return news
