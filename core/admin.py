from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Request)
admin.site.register(Reply)
admin.site.register(Vote)