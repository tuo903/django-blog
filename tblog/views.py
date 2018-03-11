from django.shortcuts import render,get_object_or_404
from .models import BlogArticles
from django.http import Http404
# Create your views here.

def blog_title(request):
	blogs=BlogArticles.objects.all()
	return render(request,'tblog/titles.html',{"blogs":blogs})

def blog_article(request,article_id):
	# article=BlogArticles.objects.get(id=article_id)
	try:
		article=get_object_or_404(BlogArticles,pk=article_id)
		pub=article.publish
	except BlogArticles.DoesNotExist:
		raise Http404("No MyModel matches the given query.")
	return render(request,'tblog/content.html',{"article":article,'publish':pub})