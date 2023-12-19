from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView, \
    PasswordChangeView, PasswordResetDoneView, PasswordResetCompleteView

from abs.views import PostViewSet
from system.views import ProfileViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'profiles', ProfileViewSet, basename='profile')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('abs.urls')),
    path('', include('system.urls')),
    path('api/', include(router.urls)),
    path('api/login/', LoginView.as_view(), name='api_login'),
    path('api/logout/', LogoutView.as_view(), name='api_logout'),
    path('api/password/reset/', PasswordResetView.as_view(), name='api_password_reset'),
    path('api/password/reset/done/', PasswordResetDoneView.as_view(), name='api_password_reset_done'),
    path('api/password/reset/confirm/', PasswordResetConfirmView.as_view(), name='api_password_reset_confirm'),
    path('api/password/reset/complete/', PasswordResetCompleteView.as_view(), name='api_password_reset_complete'),
    path('api/password/change/', PasswordChangeView.as_view(), name='api_password_change'),
]
