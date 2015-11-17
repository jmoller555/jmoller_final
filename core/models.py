from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Request(models.Model):
  course_code = models.CharField(max_length=300)
  topic_description = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User)

  def __unicode__(self):
    return self.course_code
