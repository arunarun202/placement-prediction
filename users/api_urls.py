from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import api_views

urlpatterns = [
    # Auth
    path('auth/register/', api_views.api_register, name='api-register'),
    path('auth/login/', api_views.api_login, name='api-login'),
    path('auth/logout/', api_views.api_logout, name='api-logout'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='api-token-refresh'),
    path('auth/user/', api_views.api_user, name='api-user'),

    # Profile
    path('profile/', api_views.api_profile, name='api-profile'),

    # Predictions
    path('predict/', api_views.api_predict, name='api-predict'),
    path('predictions/', api_views.api_predictions, name='api-predictions'),

    # Resume
    path('resume/upload/', api_views.api_resume_upload, name='api-resume-upload'),
    path('resume/<int:pk>/', api_views.api_resume_result, name='api-resume-result'),
    path('resumes/', api_views.api_resumes, name='api-resumes'),
    path('resume/<int:pk>/delete/', api_views.api_resume_delete, name='api-resume-delete'),

    # Chatbot
    path('chatbot/', api_views.api_chatbot, name='api-chatbot'),
]
