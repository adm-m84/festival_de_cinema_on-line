from django.contrib import admin

from .models import *


class RealizadorAdmin(admin.ModelAdmin):
    model = RealizadorModel


admin.site.register(RealizadorModel, RealizadorAdmin)
