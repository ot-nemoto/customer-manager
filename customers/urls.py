from django.urls import path
from . import views
from rest_framework import routers
from .views import CompanyViewSet, SectionViewSet, PersonViewSet

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'sections', SectionViewSet)
router.register(r'persons', PersonViewSet)

app_name = 'customers'
urlpatterns = [
    path('', views.index, name="index"),
    path('companies/', views.companies, name="companies"),
    path('companies/<int:id>/', views.company, name="company"),
    path('persons/', views.persons, name="persons"),
]
