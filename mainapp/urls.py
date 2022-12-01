from django.urls import path
from .views import home_page, success_page, failed_page

urlpatterns = [
    path('', home_page, name="home_page"),
    path('success/<str:pk>/', success_page, name="success_page"),
    path('failed/', failed_page, name="failed_page"),
]