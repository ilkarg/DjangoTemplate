from modules.module_news.orm.model.news.news import News

class RequestCreateNews:
    def execute(title, body):
        news = News(title=title, body=body)
        news.save()
        return news
