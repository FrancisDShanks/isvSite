from django.conf.urls import url

from . import views

app_name = 'zendesk'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^posts/$', views.Posts.as_view(), name='posts'),
    url(r'^OXPd_NET_Java/$', views.NetJava.as_view(), name='NET_Java'),
    url(r'^OXPd_JS/$', views.JavaS.as_view(), name='JS'),
    url(r'^OXPd_Jedi/$', views.Jedi.as_view(), name='Jedi'),
    url(r'^Samsung/$', views.Sam.as_view(), name='Samsung'),
    url(r'^OXPd_Pro/$', views.Pro.as_view(), name='Pro'),
    url(r'^OXPw_SaaS/$', views.SaaS.as_view(), name='SaaS'),
    url(r'^OXPd_Pub/$', views.PublicSdk.as_view(), name='Pub'),
    url(r'^post/(?P<p_id>[0-9]+)/$', views.post_detail, name='post_detail'),
]