from django.urls import path
from . import views


app_name: str = 'users'

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('signup/', views.sign_up, name='signup'),
    path('password/change/', views.CustomPasswordChangeView.as_view(), name='password_change'),
    path('password/change/done/', views.CustomPasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password/reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password/reset/done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password/reset/confirm/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password/reset/complete/', views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('profile/<int:id>/', views.ProfileView.as_view(), name='profile'),
]
