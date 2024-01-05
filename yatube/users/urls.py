from django.urls import path
from . import views


app_name: str = 'users'

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('signup/', views.sign_up, name='signup'),
    path('profil/<int:id>', views.ProfilView.as_view(), name='profil'),
]
