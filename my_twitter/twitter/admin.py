from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Tweet
# Register your models here.
admin.site.unregister(Group)

class ProfileInLine(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInLine]
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

#admin.site.register(Profile)

#combinando o user com profile infos

admin.site.register(Tweet)