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
    #path('companies/<int:id>/', views.company, name="company"),
    #path('companies/edit/<int:id>/', views.edit_company, name="edit_company"),
    #path('companies/save/<int:id>/', views.save_company, name="save_company"),
    path('persons/', views.persons, name="persons"),

    path('company/<int:pk>/', views.CompanyDetail.as_view(), name='company_detail'),
    path('company/new/', views.CompanyCreate.as_view(), name='company_create'),
    path('company/edit/<int:pk>/', views.CompanyUpdate.as_view(), name='company_update'),
]
