from django.shortcuts import render_to_response, get_object_or_404, HttpResponse
from article.models import Article
from datetime import datetime
from django.template import loader,RequestContext
# Create your views here.


def home(request):
    post_list = Article.objects.all()
    return render_to_response('home.html', {'post_list': post_list})


def detail(request, my_args):
    post = Article.objects.all()[int(my_args)]
    str = ("title = %s, category = %s, date_time = %s, content = %s" %
           (post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)
