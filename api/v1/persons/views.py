from django.shortcuts import render
from .models import Person
from rest_framework import viewsets, filters
from .serializer import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
