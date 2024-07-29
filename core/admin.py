from django.contrib import admin
from .models import *

admin.site.register(CoreUser)
admin.site.register(Message)
admin.site.register(Room)