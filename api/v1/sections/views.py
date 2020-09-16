from django.shortcuts import render
from .models import Section
from rest_framework import viewsets, filters
from .serializer import SectionSerializer


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
