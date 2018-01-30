from django.conf.urls import url

from . import views

app_name = 'zendesk'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^post/(?P<p_id>[0-9]+)/$', views.post_detail, name='post_detail'),
]