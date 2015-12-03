from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import *

# Create your views here.
class Home(TemplateView):
  template_name = "home.html"

class RequestCreateView(CreateView):
  model = Request
  template_name = "request/request_form.html"
  fields = ['course_code', 'topic_description']
  success_url = reverse_lazy('request_list')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(RequestCreateView, self).form_valid(form)

class RequestListView(ListView):
  model = Request
  template_name = "request/request_list.html"

class RequestDetailView(DetailView):
  model = Request
  template_name = 'request/request_detail.html'

  def get_context_data(self, **kwargs):
    context = super(RequestDetailView, self).get_context_data(**kwargs)
    request = Request.objects.get(id=self.kwargs['pk'])
    replies = Reply.objects.filter(request=request)
    context['replies'] = replies
    return context

class RequestUpdateView(UpdateView):
  model = Request
  template_name = 'request/request_form.html'
  fields = ['course_code', 'topic_description']

class RequestDeleteView(DeleteView):
  model = Request
  template_name = 'request/request_confirm_delete.html'
  success_url = reverse_lazy('request_list')

class ReplyCreateView(CreateView):
  model = Reply
  template_name = "reply/reply_form.html"
  fields = ['rate_per_hour', 'course_experience']

  def get_success_url(self):
    return self.object.request.get_absolute_url()

  def form_valid(self, form):
    form.instance.user = self.request.user
    form.instance.request = Request.objects.get(id=self.kwargs['pk'])
    return super(ReplyCreateView, self).form_valid(form)

class ReplyUpdateView(UpdateView):
  model= Reply
  pk_url_kwarg = 'reply_pk'
  template_name = 'reply/reply_form.html'
  fields = ['rate_per_hour', 'course_experience']

  def get_success_url(self):
    return self.object.request.get_absolute_url()