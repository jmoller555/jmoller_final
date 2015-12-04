from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

VISIBILITY_CHOICES = (
(0, 'Public'),
(1, 'Anonymous'),
)

# Create your models here.
class Request(models.Model):
  course_code = models.CharField(max_length=300)
  topic_description = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User)
  visibility = models.IntegerField(choices=VISIBILITY_CHOICES, default=0)

  def __unicode__(self):
    return self.course_code

  def get_absolute_url(self):
    return reverse("request_detail", args=[self.id])

class Reply(models.Model):
  request = models.ForeignKey(Request)
  user = models.ForeignKey(User)
  created_at = models.DateTimeField(auto_now_add=True)
  rate_per_hour = models.CharField(max_length=300)
  course_experience = models.TextField(null=True, blank=True)
  visibility = models.IntegerField(choices=VISIBILITY_CHOICES, default=0)

  def __unicode__(self):
    return self.rate_per_hour

class Vote(models.Model):
  user = models.ForeignKey(User)
  request = models.ForeignKey(Request, blank=True, null=True)
  reply = models.ForeignKey(Reply, blank=True, null=True)

  def __unicode__(self):
    return "%s upvoted" % (self.user.username)