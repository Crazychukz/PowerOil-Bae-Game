from django.contrib import admin
from .models import *

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('ans01', 'ans02', 'ans03')


admin.site.register(Test, ProfileAdmin)
