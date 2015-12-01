from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
class Request(models.Model):
  course_code = models.CharField(max_length=300)
  topic_description = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User)

  def __unicode__(self):
    return self.course_code

  def get_absolute_url(self):
    return reverse("request_detail", args=[self.id])