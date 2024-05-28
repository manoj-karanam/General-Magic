from backend.views import register_user,user_login
from django.urls import path

urlpatterns = [
    # Other URL patterns...
    path('register/', register_user, name='register_user'),
    path('login/', user_login, name='user_login'),

    
]
