from django.contrib import admin

from .models import IsvPosts
from .models import IsvComments
from .models import DBUpdateTime
# Register your models here.

# admin.site.register(IsvPosts)
# admin.site.register(IsvComments)
admin.site.register(DBUpdateTime)

