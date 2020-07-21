from rest_framework import routers
from .views import UserViewSet, ProfileViewSet

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('profile', ProfileViewSet)

urlpatterns = router.urls
