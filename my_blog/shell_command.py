# _*_coding:utf-8_*_

from article.models import Article
# 为数据库增加操作
Article.objects.create(
    title='Hello world', catetory='Python', content='我们来做一个简易数据库怎加操作')
Article.objects.create(
    title='Django Study', catetory='Django', content='一个简单的DjangoBlog构架')
# all and get 数据库查看操作
# 返回全部对象 返回一个列表 若无对象怎返回[]
Article.objects.all()
# 返回符合条件的对象
Article.objects.get(id=1)
# update数据库修改操作
first = Article.objects.get(id=1)
# return title
first.title
first.title = 'Hello one'
first.title
# 选择全部对象
Blog.objects.all()
# 使用filter()按题目过滤
Blog.objects.filter(caption='blogname')
# 按多个条件进行过滤
Blog.objects.filter(caption='blogname', id=1)
# 以上是精确查找 可进行包含行查找
Blog.objects.filter(caption_contains='blogname')
# 获取单个对象 若查询没有则抛出异常
Blog.objects.get(caption='blogname')
# sort data
Blog.objects.order_by('caption')
Blog.objects.order_by('-caption')
# 若以多个条件进行排序(no2 以 no1满足条件(字段值相同)下才使用到)
Blog.objects.order_by('caption', 'id')
# 连锁查询
Blog.objects.filter(caption_contains='blogname').order_by('-id')
# 限制返回数据
Blog.objects.filter(caption_contains='blogname')[0]
# 甚至 类似列表操作
Blog.objects.filter(caption_contains='blogname')[0:3]
