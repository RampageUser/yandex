from django.urls import path
from .views import get_main_page, get_group

urlpatterns = [
    path('', get_main_page),
    path('group/', get_group),
]
