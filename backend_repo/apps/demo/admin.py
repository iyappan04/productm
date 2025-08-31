from django.contrib import admin
from apps.demo.models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)