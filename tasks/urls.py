from django.conf.urls import url
from . import views


# current issues:
# index url prevents detail page
# addTask not working properly anymore after index was updated

app_name = 'tasks'
urlpatterns = [
    url(r'^(?P<task_type>\w*)/$', views.IndexView.as_view(), name='index'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^complete/$', views.complete, name='complete'),
    url(r'^addTask/$', views.addTask, name='addTask'),
    url(r'^editTask/$', views.editTask, name='editTask'),
    url(r'^deleteTask/$', views.deleteTask, name='deleteTask'),
]