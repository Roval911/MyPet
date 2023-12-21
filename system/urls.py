from django.urls import path
from .views import *

urlpatterns = [
    # Django Views URLs
    path('profile/<slug:slug>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('register/', UserRegisterView.as_view(), name='register'),

    # Django REST Framework URLs
    path('api/login/', UserLoginAPIView.as_view(), name='api_login'),
    path('api/logout/', UserLogoutAPIView.as_view(), name='api_logout'),
    path('api/profile/', ProfileAPIView.as_view(), name='profile_api'),
    path('api/register/', UserRegisterAPIView.as_view(), name='user_register_api'),
    path('api/confirm-email/<str:uidb64>/<str:token>/', UserConfirmEmailAPIView.as_view(), name='api_confirm_email'),

    # Other Django Views URLs (You can add more as needed)
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('change-password/', UserPasswordChangeView.as_view(), name='password_change'),
    path('forgot-password/', UserForgotPasswordView.as_view(), name='password_reset'),
    path('reset-password-confirm/<str:uidb64>/<str:token>/', UserPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('confirm-email/<str:uidb64>/<str:token>/', UserConfirmEmailView.as_view(), name='confirm_email'),

    # Other Django Views URLs (You can add more as needed)
    path('email-confirmation-sent/', EmailConfirmationSentView.as_view(), name='email_confirmation_sent'),
    path('email-confirmed/', EmailConfirmedView.as_view(), name='email_confirmed'),
    path('email-confirmation-failed/', EmailConfirmationFailedView.as_view(), name='email_confirmation_failed'),
    path('feedback/', FeedbackCreateView.as_view(), name='feedback'),
]