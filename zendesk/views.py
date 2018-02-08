from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import *
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.http import StreamingHttpResponse

import json

# Create your views here.


def index(request):
    # posts = models.IsvPosts.objects.all()
    # return render(request, "zendesk/index.html", {"data": posts})
    t = DBUpdateTime.objects.order_by("-timestamp")[:1]
    # t is <QuerySet [<DBUpdateTime: DBUpdateTime object>]>
    context = {'latest': t[0]}
    return render(request, 'zendesk/index.html', context)


def download_posts(request):
    def file_iterator(file_name, chunk_size=512):  # 用于形成二进制数据
        with open(file_name, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    doc_url = "static/docs/"
    t = DBUpdateTime.objects.order_by("-timestamp")[:1][0].date
    t = t.replace('/', '_')
    the_file_name = "posts_" + t + ".xls"
    print(the_file_name)
    response = StreamingHttpResponse(file_iterator(doc_url + the_file_name))  # 这里创建返回
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment; filename="{0}"'.format(the_file_name)
    return response


def download_comments(request):
    def file_iterator(file_name, chunk_size=512):  # 用于形成二进制数据
        with open(file_name, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    doc_url = "static/docs/"
    t = DBUpdateTime.objects.order_by("-timestamp")[:1][0].date
    t = t.replace('/', '_')
    the_file_name = "comments_" + t + ".xls"
    print(the_file_name)
    response = StreamingHttpResponse(file_iterator(doc_url + the_file_name))  # 这里创建返回
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment; filename="{0}"'.format(the_file_name)
    return response


def search(request):
    context = {}
    if request.method == "GET":
        postid = request.GET.get("postid", None)
        try:
            searchr = IsvPosts.objects.get(pk=postid)
            context['search'] = searchr
        except IsvPosts.DoesNotExist:
            pass
    return render(request, 'zendesk/search.html', context)


def login(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        ZendeskUserInfo.objects.create(user=username, pwd=password)
    user_list = ZendeskUserInfo.objects.all()
    return render(request, "zendesk/login.html", {"data": user_list})


def post_detail(request, p_id):
    post = get_object_or_404(IsvPosts, pk=p_id)
    # TODO: users list from zendesk not completes, I can only show unknown for those users
    try:
        uname = IsvUsers.objects.get(id=post.author_id).name
    except IsvUsers.DoesNotExist:
        uname = "Unknown"

    post.author_id = uname
    post.topic_id = IsvTopics.objects.get(id=post.topic_id).name
    comments = IsvComments.objects.filter(post_id=p_id)
    for c in comments:
        try:
            uname = IsvUsers.objects.get(id=c.author_id).name
        except IsvUsers.DoesNotExist:
            uname = "Unknown"
        c.author_id = uname
    # comment = get_list_or_404(IsvComments, post_id=p_id)
    return render(request, "zendesk/post_detail.html", {'post': post, 'comments': comments})


class Posts(generic.ListView):
    template_name = 'zendesk/posts.html'
    context_object_name = 'data'

    def get_queryset(self):
        return IsvPosts.objects.order_by('-updated_at_timestamp')[:]


class NetJava(generic.ListView):
    template_name = 'zendesk/oxpd_netjava.html'
    context_object_name = 'data'

    def get_queryset(self):
        return IsvPosts.objects.filter(topic_id='115000131927')


class JavaS(generic.ListView):
    template_name = 'zendesk/oxpd_javascript.html'
    context_object_name = 'data'

    def get_queryset(self):
        return IsvPosts.objects.filter(topic_id='201036407')


class Jedi(generic.ListView):
    template_name = 'zendesk/oxpd_jedi.html'
    context_object_name = 'data'

    def get_queryset(self):
        return IsvPosts.objects.filter(topic_id='115000326907')


class Sam(generic.ListView):
    template_name = 'zendesk/samsung.html'
    context_object_name = 'data'

    def get_queryset(self):
        return IsvPosts.objects.filter(topic_id='115000542808')


class Pro(generic.ListView):
    template_name = 'zendesk/oxpd_pro.html'
    context_object_name = 'data'

    def get_queryset(self):
        return IsvPosts.objects.filter(topic_id='115000330548')


class SaaS(generic.ListView):
    template_name = 'zendesk/oxpw_saas.html'
    context_object_name = 'data'

    def get_queryset(self):
        return IsvPosts.objects.filter(topic_id='115000329828')


class PublicSdk(generic.ListView):
    template_name = 'zendesk/public_sdks.html'
    context_object_name = 'data'

    def get_queryset(self):
        return IsvPosts.objects.filter(topic_id='115000399268')
