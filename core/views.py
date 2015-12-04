from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.views.generic import FormView
from .models import *
from .forms import *

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
    user_replies = Reply.objects.filter(request=request, user=self.request.user)
    context['user_replies'] = user_replies
    return context

class RequestUpdateView(UpdateView):
  model = Request
  template_name = 'request/request_form.html'
  fields = ['course_code', 'topic_description']

  def get_object(self, *args, **kwargs):
    object = super(RequestUpdateView, self).get_object(*args, **kwargs)
    if object.user != self.request.user:
      raise PermissionDenied()
    return object

class RequestDeleteView(DeleteView):
  model = Request
  template_name = 'request/request_confirm_delete.html'
  success_url = reverse_lazy('request_list')

  def get_object(self, *args, **kwargs):
    object = super(RequestDeleteView, self).get_object(*args, **kwargs)
    if object.user != self.request.user:
      raise PermissionDenied()
    return object

class ReplyCreateView(CreateView):
  model = Reply
  template_name = "reply/reply_form.html"
  fields = ['rate_per_hour', 'course_experience']

  def get_success_url(self):
    return self.object.request.get_absolute_url()

  def form_valid(self, form):
    request = Request.objects.get(id=self.kwargs['pk'])
    if Reply.objects.filter(request=request, user=self.request.user).exists():
      raise PermissionDenied()
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

  def get_object(self, *args, **kwargs):
    object = super(ReplyUpdateView, self).get_object(*args, **kwargs)
    if object.user != self.request.user:
      raise PermissionDenied()
    return object

class ReplyDeleteView(DeleteView):
  model = Reply
  pk_url_kwarg = 'reply_pk'
  template_name = 'reply/reply_confirm_delete.html'

  def get_success_url(self):
    return self.object.request.get_absolute_url()

  def get_object(self, *args, **kwargs):
    object = super(ReplyDeleteView, self).get_object(*args, **kwargs)
    if object.user != self.request.user:
      raise PermissionDenied()
    return object

class VoteFormView(FormView):
  form_class = VoteForm

  def form_valid(self, form):
    user = self.request.user
    request = Request.objects.get(pk=form.data["request"])
    try:
      reply = Reply.objects.get(pk=form.data["reply"])
      prev_votes = Vote.objects.filter(user=user, request=request)
      has_voted = (prev_votes.count()>0)
      if not has_voted:
        Vote.objects.create(user=user, request=request)
      else:
        prev_votes[0].delete()
      return redirect(reverse('request_detail', args=[form.data["request"]]))
    except:
      prev_votes = Vote.objects.filter(user=user, request=request)
      has_voted = (prev_votes.count()>0)
      if not has_voted:
        Vote.objects.create(user=user, request=request)
      else:
        prev_votes[0].delete()
    return redirect('request_list')

class UserDetailView(DetailView):
  model = User
  slug_field = 'username'
  template_name = 'user/user_detail.html'
  context_object_name = 'user_in_view'

  def get_context_data(self, **kwargs):
    context = super(UserDetailView, self).get_context_data(**kwargs)
    user_in_view = User.objects.get(username=self.kwargs['slug'])
    requests = Request.objects.filter(user=user_in_view)
    context['requests'] = requests
    replies = Reply.objects.filter(user=user_in_view)
    context['replies'] = replies
    return context

class UserUpdateView(UpdateView):
  model = User
  slug_field = "username"
  template_name = "user/user_form.html"
  fields = ['email', 'first_name', 'last_name']

  def get_success_url(self):
    return reverse('user_detail', args=[self.request.user.username])

  def get_object(self, *args, **kwargs):
    object = super(UserUpdateView, self).get_object(*args, **kwargs)
    if object != self.request.user:
      raise PermissionDenied()
    return object