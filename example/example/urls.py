from django.conf.urls import url

from app import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^example/([0-9A-Za-z\-]+)', views.example, name='example'),
]
