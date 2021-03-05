from django.db import models


# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=64, verbose_name="标题")
	abstract = models.CharField(max_length=128, verbose_name="摘要")
	content = models.TextField(verbose_name="内容")
	
	def __str__(self):
		return "{}".format(self.title)
	
	@classmethod
	def articles_to_dict(cls, articles):
		arts = {}
		for article in articles:
			tmp = {}
			tmp['title'] = article.title
			tmp['abstract'] = article.abstract
			tmp['content'] = article.content
			arts[article.id] = tmp
		return arts
