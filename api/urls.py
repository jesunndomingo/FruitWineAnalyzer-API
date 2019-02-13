from django.conf.urls import url
from django.urls import path
from . import views
from .serializers import UpdateSerializer, HistorySerializer

urlpatterns=[
url(r'^postData/$', views.upload_data.as_view()),
url(r'^getData/$', views.result_list.as_view()),
url(r'^updateData/(?P<id>[-\w]+)/$', views.update_list.as_view()),
url(r'^deleteData/(?P<pk>\d+)/$', views.delete_history.as_view())
]