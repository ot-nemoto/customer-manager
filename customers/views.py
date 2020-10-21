from django.shortcuts import render, redirect
from .models import Company, Section, Person
from rest_framework import viewsets, filters
from .serializer import CompanySerializer, SectionSerializer, PersonSerializer

from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q

from .forms import CompanyForm, SectionForm, PersonForm
from django.views.generic import DetailView, CreateView, UpdateView
from django.urls import reverse
from django.http import JsonResponse
import json
import logging

logger = logging.getLogger(__name__)

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

def section_list(request):
    logging.debug(request)
    company_id=request.GET.get('company_id')
    sections = Section.objects.all()
    if company_id is not None and company_id.isdecimal():
        sections = sections.filter(company_id=company_id)
    data = {
        'sections': [{'id': section.pk, 'name': section.name} for section in sections]
    }
    return HttpResponse(json.dumps(data, ensure_ascii=False),content_type='application/json')

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





class CompanyDetail(DetailView):
    model = Company
    template_name = "company/detail.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['sections'] = Section.objects.filter(company_id=self.kwargs['pk'])
        ctx['persons'] = Person.objects.filter(company_id=self.kwargs['pk'])
        return ctx

class CompanyCreate(CreateView):
    model = Company
    form_class = CompanyForm
    template_name = "company/create.html"

    def get_success_url(self):
        return reverse('customers:company_detail', kwargs={'pk': self.object.pk})

class CompanyUpdate(UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = "company/update.html"

    def get_success_url(self):
        return reverse('customers:company_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['sections'] = Section.objects.filter(company_id=self.kwargs['pk'])
        ctx['persons'] = Person.objects.filter(company_id=self.kwargs['pk'])
        return ctx

class SectionDetail(DetailView):
    model = Section
    template_name = "section/detail.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['persons'] = Person.objects.filter(section_id=self.kwargs['pk'])
        return ctx

class SectionCreate(CreateView):
    model = Section
    form_class = SectionForm
    template_name = "section/create.html"

    def get_success_url(self):
        return reverse('customers:section_detail', kwargs={'pk': self.object.pk})

class SectionUpdate(UpdateView):
    model = Section
    form_class = SectionForm
    template_name = "section/update.html"

    def get_success_url(self):
        return reverse('customers:section_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['persons'] = Person.objects.filter(section_id=self.kwargs['pk'])
        return ctx

class PersonDetail(DetailView):
    model = Person
    template_name = "person/detail.html"

class PersonCreate(CreateView):
    model = Person
    form_class = PersonForm
    template_name = "person/create.html"

    def get_success_url(self):
        return reverse('customers:person_detail', kwargs={'pk': self.object.pk})

class PersonUpdate(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = "person/update.html"

    def get_success_url(self):
        return reverse('customers:person_detail', kwargs={'pk': self.object.pk})
