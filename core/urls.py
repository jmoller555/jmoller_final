from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
  url(r'^$', Home.as_view(), name='home'),
  url(r'^user/', include('registration.backends.simple.urls')),
  url(r'^user/', include('django.contrib.auth.urls')),
  url(r'^request/create/$', RequestCreateView.as_view(), name='request_create'),
  url(r'^request/$', RequestListView.as_view(), name='request_list'),
  url(r'^request/(?P<pk>\d+)/$', RequestDetailView.as_view(), name='request_detail'),
  url(r'^request/update/(?P<pk>\d+)/$', RequestUpdateView.as_view(), name='request_update'),
  url(r'^request/delete/(?P<pk>\d+)/$', RequestDeleteView.as_view(), name='request_delete'),
  url(r'^request/(?P<pk>\d+)/reply/create/$', ReplyCreateView.as_view(), name='reply_create'),
  url(r'^request/(?P<request_pk>\d+)/reply/update/(?P<reply_pk>\d+)/$', ReplyUpdateView.as_view(), name='reply_update'),
  url(r'^request/(?P<request_pk>\d+)/reply/delete/(?P<reply_pk>\d+)/$', ReplyDeleteView.as_view(), name='reply_delete'),
)