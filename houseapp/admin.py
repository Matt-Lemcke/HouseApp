from django.contrib import admin

# Register your models here.
from houseapp.models import *

admin.site.register(House)
admin.site.register(Task)
admin.site.register(Membership)
admin.site.register(Message)
admin.site.register(Notification)