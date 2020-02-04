from django.urls import path, include
from .views import home, proposal, access, notification
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('allauth.urls')),
    path('project/access/', access, name='access'),
    path('project/notif/', notification, name='notification'),
    path('project/<slug:the_slug>/', proposal, name='proposal'),

]