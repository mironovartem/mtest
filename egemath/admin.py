from django.contrib import admin
from .models import EgeMathTest, UserAccessLevel
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UserAccessLevelInline(admin.StackedInline):
    model = UserAccessLevel
    can_delete = False
    verbose_name_plural = 'UserAccessLevel'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserAccessLevelInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register your models here.
admin.site.register(EgeMathTest)
admin.site.register(UserAccessLevel)
