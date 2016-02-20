from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.loginrequest, name='loginrequest'),
    #url(r'^$', views.login, name='login'),
]
