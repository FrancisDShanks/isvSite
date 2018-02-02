from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import IsvTopics, IsvUsers, IsvPosts, IsvComments, ZendeskUserInfo
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

import json

# Create your views here.


def index(request):
    # posts = models.IsvPosts.objects.all()
    # return render(request, "zendesk/index.html", {"data": posts})

    context = {}
    if request.method == "GET":
        postid = request.GET.get("postid", None)
        try:
            searchr = IsvPosts.objects.get(pk=postid)
            context['search'] = searchr
        except IsvPosts.DoesNotExist:
            pass
    return render(request, 'zendesk/index.html', context)


def login(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        ZendeskUserInfo.objects.create(user=username, pwd=password)

    user_list = models.ZendeskUserInfo.objects.all()
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
