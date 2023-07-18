from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import customerViewSet, rocketViewSet, payloadViewSet, launchViewSet

router = DefaultRouter()

router.register(r'customer', customerViewSet, basename='customer')
router.register(r'rocket', rocketViewSet, basename='rocket')
router.register(r'payload', payloadViewSet, basename='payload')
router.register(r'launch', launchViewSet, basename='launch')


urlpatterns = [
    path('', include(router.urls)),
 ]