from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Project, Subject, Membership, CustomUser, Notification
# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm


admin.site.register(Subject)
admin.site.register(Project)
admin.site.register(Membership)
admin.site.register(Notification)
admin.site.register(CustomUser, CustomUserAdmin)



