from django.contrib import admin

from instagram.models import Post, InstaUser

# Register your models here.
admin.site.register(Post)
admin.site.register(InstaUser)