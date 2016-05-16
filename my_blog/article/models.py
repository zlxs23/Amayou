# _*_coding:utf-8_*_

from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Article(models.Model):

    """docstring for Article"""
    title = models.CharField(max_length=100)  # 题目
    category = models.CharField(max_length=50, blank=True)  # 标签
    date_time = models.DateTimeField(auto_now_add=True)	   # 时间
    content = models.TextField(blank=True, null=True)  # 正文

    def get_absolute_url(self):
        path = reverse('detail',kwargs={'id':self.id})
        return 'http://127.0.0.1:8000%s' % path

    def __unicode__(self):
        return self.title

    class Meta:

        """按时间下降排序"""
        ordering = ['-date_time']
