from django.conf.urls import include, url

urlpatterns = (
    url(r'^', include('testproject.myapp.urls')),
)
