from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import WorkViewSet, RegisterAPI

router = routers.DefaultRouter()
router.register('works', WorkViewSet, basename='work')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/register/', RegisterAPI.as_view()),
]
