from django.urls import path
from . import views


app_name: str = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.create_post, name='post'),
    path('post/delete/<int:id>', views.DeletePostView.as_view(), name='delete'),
    path('groups/<slug:slug>', views.group_posts, name='group_list'),
]
