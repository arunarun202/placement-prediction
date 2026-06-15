from django.urls import path
from .views import home,index, profile, RegisterView,logout_view
from . import views

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('logout_view/',logout_view,name='logout_view'),
    path('index/', index, name='users-index'),
    path('Model/', views.Model, name='Model'),
    path('Database/', views.Database, name='Database'),
    path('Report/',views.Report,name='Report'),
    path('chatbot/', views.chatbot_response_view,name='chatbot'),
    path('upload/', views.upload_resume, name='upload_resume'),
    path('result/<int:pk>/', views.resume_result, name='resume_result'),
    path('resumes/', views.resume_database, name='resume_list'),
    path('resumes/delete/<int:id>/', views.delete_resume, name='delete_resume'),
    
    
    
    
    ]


 