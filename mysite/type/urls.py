from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/$',views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
	url(r'^createsummary/(?P<pk>\d+)/$',views.get_name,name='get_name'),
	url(r'^post/(?P<pk>^.+/$)', views.post_detail, name='post_detail'),
	url(r'^post/applying/$', views.apply_new, name='apply'),
	url(r'^post/validate/$', views.validate, name='validate'),
	url(r'choice/', views.choice_new, name='choice'),
]