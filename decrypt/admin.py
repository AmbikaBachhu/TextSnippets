from django.contrib import admin
from .models import Snippet
# Register your models here.


class Snippetadmin(admin.ModelAdmin):
    list_display = ['id','created','title','code','owner']


admin.site.register(Snippet,Snippetadmin)