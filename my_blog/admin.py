from django.contrib import admin
from my_blog.models import Post,Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)