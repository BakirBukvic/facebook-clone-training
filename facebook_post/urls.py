from django.urls import path
from .views import post_list

app_name = 'facebook_post'

urlpatterns = [
    path('', post_list, name='post_list'),
]