from django.shortcuts import render,get_object_or_404
from .models import BlogArticles
from django.http import Http404
# Create your views here.

def blog_title(request):
	blogs=BlogArticles.objects.all()
	return render(request,'tblog/titles.html',{"blogs":blogs})

def blog_article(request,article_id):
	# article=BlogArticles.objects.get(id=article_id)

	article=BlogArticles.objects.get(id=article_id)
	pub=article.publish
  
	return render(request,'tblog/content.html',{"article":article,'publish':pub})