from django.contrib import admin

from .models import IsvPosts
from .models import IsvComments
# Register your models here.

admin.site.register(IsvPosts)
admin.site.register(IsvComments)

