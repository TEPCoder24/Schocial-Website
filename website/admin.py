from django.contrib import admin
from .models import PostModel, ProfileModel


class PostAdmin(admin.ModelAdmin):
    list_display = ['username', 'text']

class ProfileAdmin(admin.ModelAdmin):
    list_display= ["username", "grade"]

# Register your models here.
admin.site.register(PostModel, PostAdmin)
admin.site.register(ProfileModel, ProfileAdmin)