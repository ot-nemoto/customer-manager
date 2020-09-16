from django.shortcuts import render
from .models import Company
from rest_framework import viewsets, filters
from .serializer import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
