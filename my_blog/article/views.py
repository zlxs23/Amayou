from django.shortcuts import render_to_response, get_object_or_404, HttpResponse
from article.models import Article
from datetime import datetime
from django.template import loader, RequestContext
from django.http import Http404
# Create your views here.


def home(request):
    post_list = Article.objects.all()
    return render_to_response('home.html', {'post_list': post_list})


def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExit:
        raise Http404
    return render_to_response('post.html', {'post': post})


def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExit:
        raise Http404
    return render_to_response('archives.html', {'post_list': post_list, 'error': False})


def about_me(request):
    return render(request, 'aboutme.html')


def search_tag(request, tag):
    try:
        post_list = Article.objects.filter(category__iexact=tag)  # contains
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'tag.html', {'post_list': post_list})
