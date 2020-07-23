from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'date_post', 'id']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'id']


admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)
