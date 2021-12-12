from django.conf.urls import url
from rest_framework import routers, urlpatterns
from users.views import UserViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = router.urls