from backend import views
from django.urls import path

urlpatterns = [
    # Other URL patterns...
    path('register/', views.register_user, name='register_user'),
    path('login/', views.user_login, name='user_login'),
    path('add-experience/', views.add_experience, name='add_experience'),
    path('edit-experience/<int:experience_id>/', views.edit_experience, name='edit_experience'),
    
]
