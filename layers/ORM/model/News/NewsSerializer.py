from rest_framework import serializers
from layers.ORM.model.News.News import News

class NewsSerializer(serializers.ModelSerializer):
	class Meta:
		model = News
		fields = '__all__'