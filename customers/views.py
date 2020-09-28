from django.shortcuts import render
from .models import Company, Section, Person
from rest_framework import viewsets, filters
from .serializer import CompanySerializer, SectionSerializer, PersonSerializer

from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q

def index(request):
    return render(request, 'index.html', {})

def companies(request):
    page_num = request.GET.get('p') or 1
    index_name = request.GET.get('i')
    search = request.GET.get('q')
    companies = Company.objects.order_by('-update_date')
    if index_name is not None:
        companies = companies.filter(index_name=index_name)
    if search is not None:
        companies = companies.filter(Q(name__icontains=search)|Q(search_name__icontains=search))
    context = {
        'companies': Paginator(companies, 50).page(page_num),
        'index_name_choices': Company.INDEX_NAME_CHOICES,
    }
    return render(request, 'companies.html', context)

def company(request, id):
    context = {
        'company': Company.objects.get(id=id),
    }
    return render(request, 'company.html', context)

def persons(request):
    return HttpResponse("persons")

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
