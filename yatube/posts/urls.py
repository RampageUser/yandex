from django.urls import path
from .views import index, group_posts

app_name = 'posts'

urlpatterns = [
    path('', index, name='main'),
    path('group/', group_posts, name='group'),
]
