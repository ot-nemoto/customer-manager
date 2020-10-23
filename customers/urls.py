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
    path('persons/', views.persons, name="persons"),

    path('companiess/', views.CompanyList.as_view(), name='company_list'),
    path('companiess/<int:index_name>/', views.CompanyList.as_view(), name='company_list'),
    path('company/', views.CompanyCreate.as_view(), name='company_create'),
    path('company/<int:pk>/', views.CompanyDetail.as_view(), name='company_detail'),
    path('company/<int:pk>/edit/', views.CompanyUpdate.as_view(), name='company_update'),

    path('section/', views.SectionCreate.as_view(), name='section_create'),
    path('section/<int:pk>/', views.SectionDetail.as_view(), name='section_detail'),
    path('section/<int:pk>/edit/', views.SectionUpdate.as_view(), name='section_update'),

    path('person/', views.PersonCreate.as_view(), name='person_create'),
    path('person/<int:pk>/', views.PersonDetail.as_view(), name='person_detail'),
    path('person/<int:pk>/edit/', views.PersonUpdate.as_view(), name='person_update'),

    path('ajax/section_list/', views.section_list, name="section_list")
]
