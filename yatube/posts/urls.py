from django.urls import path
from . import views


app_name: str = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.create_post, name='post'),
    path('post/<int:post_id>', views.post_detail, name='post_detail'),
    path('post/<str:username>', views.profile_view, name='profile'),
    path('post/delete/<int:id>', views.DeletePostView.as_view(), name='delete'),
    path('groups/<slug:slug>', views.group_posts, name='group_list'),
]
