from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'tasks'
urlpatterns = [
    url(r'^$|^(?P<task_type>day|month|year|once)/$', login_required(views.IndexView.as_view()), name='index'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^complete/$', views.complete, name='complete'),
    url(r'^addTask/$', views.addTask, name='addTask'),
    url(r'^editTask/$', views.editTask, name='editTask'),
    url(r'^deleteTask/$', views.deleteTask, name='deleteTask'),
]

