# -*- coding: utf-8 -*-
# @Time    : 2021/3/5 8:08 下午
# @Author  : AI悦创
# @FileName: api.py
# @Software: PyCharm
# @Blog    ：http://www.aiyc.top
# @公众号   ：AI悦创
from django.http import JsonResponse
from .models import Article


def export_article(request, id=None):
	if id:
		articles = Article.objects.filter(id=id)
	else:
		articles = Article.objects.all()
	articles_json = Article.articles_to_dict(articles)
	print(articles_json)
	return JsonResponse(articles_json, json_dumps_params={'ensure_ascii': False})
