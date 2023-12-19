from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from abs.views import PostViewSet


router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('abs.urls')),
    path('', include('system.urls')),
    path('api/', include(router.urls)),
]
