from django.urls import path, include
from .views import home, proposal, access
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('allauth.urls')),
    path('project/access/', access, name='access'),
    path('project/<slug:the_slug>/', proposal, name='proposal'),

]