from django.conf.urls import url
from django.urls import path
from . import views
from .serializers import mySerializer

urlpatterns=[
url(r'^postData/$', views.UploadData.as_view()),
url(r'^getData/$', views.result_list.as_view())
]