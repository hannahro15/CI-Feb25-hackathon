
from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.profile_view, name='profile_view'),
    path('edit/', views.profile_edit, name='profile_edit'),
    path('avatar/upload/', views.upload_avatar, name='upload_avatar'),
]