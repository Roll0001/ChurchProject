from auth_system import views
from django.urls import path


urlpatterns = [
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login')
]
