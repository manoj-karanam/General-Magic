from backend import views
from django.urls import path

urlpatterns = [
    # Other URL patterns...
    path('register/', views.register_user, name='register_user'),
    path('login/', views.user_login, name='user_login'),

    #user details
    path('add_user_details/', views.add_user_details, name='add_user_details'),
    path('edit_user_details/', views.edit_user_details, name='edit_user_details'),
    path('get_user_details/<str:user_id>/', views.get_user_details, name='get_user_details'),

    # experience
    path('add_experience/', views.add_experience, name='add_experience'),
    path('edit_experience/<str:user_id>/', views.edit_experience, name='edit_experience'),

    #education
    path('add_education/', views.add_education, name='add_education'),
    path('edit_education/<str:user_id>/', views.edit_education, name='edit_education')
    
]