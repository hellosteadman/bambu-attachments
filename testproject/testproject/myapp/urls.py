from django.conf.urls import url
from testproject.myapp.views import home

urlpatterns = (url(r'^', home),)
