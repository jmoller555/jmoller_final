from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
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