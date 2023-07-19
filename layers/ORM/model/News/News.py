from django.db import models

class News(models.Model):
	class Meta:
		app_label = 'project'
	title = models.CharField(max_length=255)
	body = models.TextField()