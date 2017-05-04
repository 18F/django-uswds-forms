from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'app.views.home', name='home'),
]
