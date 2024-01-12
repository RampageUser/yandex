from django.urls import path
from . import views


app_name: str = 'users'

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('signup/', views.sign_up, name='signup'),
    path('password_change/', views.CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done', views.CustomPasswordChangeDoneView.as_view(), name='password_change_done'),
    path('profile/<int:id>', views.ProfileView.as_view(), name='profile'),
]
