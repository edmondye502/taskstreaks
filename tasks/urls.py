from django.conf.urls import url

from . import views

app_name = 'tasks'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<task_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^complete/$', views.complete, name='complete'),
]