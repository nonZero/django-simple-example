from django.conf.urls import patterns, include, url

from blog import views

urlpatterns = patterns('',
    url(r'^$', views.list_posts),
    url(r'^(\d+)/$', views.show_post, name="post"),
)
