from rest_framework import serializers
from modules.module_news.orm.model.news.news import News

class NewsSerializer(serializers.ModelSerializer):
	class Meta:
		model = News
		fields = '__all__'
