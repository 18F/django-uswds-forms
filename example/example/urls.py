from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'app.views.home', name='home'),
]
