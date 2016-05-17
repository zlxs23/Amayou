from django.shortcuts import render_to_response, get_object_or_404, HttpResponse, redirect
from article.models import Article
from datetime import datetime
from django.template import loader, RequestContext
from django.http import Http404
from django.contrib.syndication.views import Feed
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def home(request):
    posts = Article.objects.all()
    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.paginator(paginator.num_pages)
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
    return render_to_response('aboutme.html')


def search_tag(request, tag):
    try:
        post_list = Article.objects.filter(category__iexact=tag)  # contains
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'tag.html', {'post_list': post_list})


def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render_to_response('home.html')
        else:
            post_list = Article.objects.filter(title__icontains=s)
            if len(post_list) == 0:
                return render_to_response('archives.html', {'post_list': post_list, 'error': True})
            else:
                return render_to_response('archives.html', {'post_list': post_list, 'error': False})
    return redirect('/')


class RSSFeed(Feed):

    """docstring for RSSFeed"""
    title = 'RSS Feed -Article'
    link = "feed/posts"
    description = 'RSS Feed -Blog Posts'

    def items(self):
        return Article.objects.order_by('-date_time')

    def item_title(self, item):
        return item.title

    def item_update(self, item):
        return item.add_date

    def item_description(self, item):
        return item.content
