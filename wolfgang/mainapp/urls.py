from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getContacts/$', views.getContacts, name='getContacts'),
    url(r'^getAccounts/$', views.getAccounts, name='getAccounts'),
    url(r'^getLeads/$', views.getLeads, name='getLeads'),
    url(r'^getPayload/$', views.getPayload, name='getPayload'),
    url(r'^getHeaders/$', views.getHeaders, name='getHeaders'),
    url(r'^getInstanceUrl/$', views.getInstanceUrl, name='getInstanceUrl'),
    url(r'^getUserInformation/$', views.getUserInformation, name='getUserInformation'),
]
