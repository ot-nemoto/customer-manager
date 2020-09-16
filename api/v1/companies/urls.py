from django.urls import path
from . import views
from rest_framework import routers
from .views import CompanyViewSet

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
