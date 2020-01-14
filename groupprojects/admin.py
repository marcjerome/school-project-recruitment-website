from django.contrib import admin

from .models import Project, Subject, Membership
# Register your models here.
admin.site.register(Subject)
admin.site.register(Project)
admin.site.register(Membership)


