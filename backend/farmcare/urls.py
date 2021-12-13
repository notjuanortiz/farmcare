"""farmcare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from alerts.views import CreateEmailAlertView
from users.views import UserViewSet, UserDashboardView, AddUserCropView
from crops.views import CropViewSet

# Loads admin.py for all apps
# Lets us customize admin panel without needing to explicitly define routes
admin.autodiscover()

router = DefaultRouter()
router.register(r'crops', CropViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'auth/', include('dj_rest_auth.urls')),
    url(r'auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('dashboard', UserDashboardView.as_view(), name='dashboard'),
    path('alerts/email/', CreateEmailAlertView.as_view(), name='alert_email'),
    path('users/add_crop/', AddUserCropView.as_view(), name='create_user_crop')
]

urlpatterns += router.urls
