from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]
    list_display = ('username', 'email', 'screenName', 'url')

    def screenName(self, obj):
        return obj.profile.screenName

    def url(self, obj):
        return obj.profile.url

    screenName.short_description = '昵称'
    url.short_description = '主页'


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
