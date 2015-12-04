from django.conf.urls import patterns, include, url
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
  url(r'^$', Home.as_view(), name='home'),
  url(r'^user/', include('registration.backends.simple.urls')),
  url(r'^user/', include('django.contrib.auth.urls')),
  url(r'^request/create/$', login_required(RequestCreateView.as_view()), name='request_create'),
  url(r'^request/$', login_required(RequestListView.as_view()), name='request_list'),
  url(r'^request/(?P<pk>\d+)/$', login_required(RequestDetailView.as_view()), name='request_detail'),
  url(r'^request/update/(?P<pk>\d+)/$', login_required(RequestUpdateView.as_view()), name='request_update'),
  url(r'^request/delete/(?P<pk>\d+)/$', login_required(RequestDeleteView.as_view()), name='request_delete'),
  url(r'^request/(?P<pk>\d+)/reply/create/$', login_required(ReplyCreateView.as_view()), name='reply_create'),
  url(r'^request/(?P<request_pk>\d+)/reply/update/(?P<reply_pk>\d+)/$', login_required(ReplyUpdateView.as_view()), name='reply_update'),
  url(r'^request/(?P<request_pk>\d+)/reply/delete/(?P<reply_pk>\d+)/$', login_required(ReplyDeleteView.as_view()), name='reply_delete'),
  url(r'^vote/$', login_required(VoteFormView.as_view()), name='vote'),
  url(r'^user/(?P<slug>\w+)/$', login_required(UserDetailView.as_view()), name='user_detail'),
)