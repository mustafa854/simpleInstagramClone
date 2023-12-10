from django.contrib import admin
from django.contrib.admin import decorators
from .models import Posts, Profile, Likes, Followers

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    pass

@admin.register(Followers)
class LikesAdmin(admin.ModelAdmin):
    pass
