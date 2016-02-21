from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^search$', views.search, name='search'),
    url(r'^nearestairport$', views.nearestairport, name='nearestairport'),
]
