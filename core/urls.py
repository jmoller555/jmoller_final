from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
  url(r'^$', Home.as_view(), name='home'),
  url(r'^user/', include('registration.backends.simple.urls')),
  url(r'^user/', include('django.contrib.auth.urls')),
  url(r'^request/create/$', RequestCreateView.as_view(), name='request_create'),
  url(r'^request/$', RequestListView.as_view(), name='request_list'),
)