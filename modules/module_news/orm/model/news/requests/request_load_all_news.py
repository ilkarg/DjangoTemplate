from modules.module_news.orm.model.news.news import News

class RequestLoadAllNews:
    def execute():
        return News.objects.values()
