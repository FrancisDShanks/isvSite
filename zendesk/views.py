from django.shortcuts import render
from django.shortcuts import HttpResponse
from zendesk import models
from django.shortcuts import get_object_or_404, get_list_or_404

import psycopg2
# Create your views here.


def index(request):
    # posts = models.IsvPosts.objects.all()
    # return render(request, "zendesk/index.html", {"data": posts})
    latest_posts = models.IsvPosts.objects.order_by('-updated_at_timestamp')[:10]
    context = {
        'data': latest_posts,
    }

    if request.method == "GET":
        postid = request.GET.get("postid", None)
        try:
            searchr = models.IsvPosts.objects.get(pk=postid)
            context['search'] = searchr
        except models.IsvPosts.DoesNotExist:
            pass
    return render(request, 'zendesk/index.html', context)


def login(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        models.ZendeskUserinfo.objects.create(user=username, pwd=password)

    user_list = models.ZendeskUserinfo.objects.all()
    return render(request, "zendesk/login.html", {"data": user_list})


def post_detail(request, p_id):
    post = get_object_or_404(models.IsvPosts, pk=p_id)
    # Don't use get_list_or_404 here, post may have no comments
    comment = models.IsvComments.objects.filter(post_id=p_id)
    # comment = get_list_or_404(models.IsvComments, post_id=p_id)
    return render(request, "zendesk/post_detail.html", {'post': post, 'comments': comment})
