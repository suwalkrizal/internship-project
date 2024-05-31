from django.shortcuts import render
from rest_framework.decorators  import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django_filters import rest_framework as filter
from rest_framework.permissions  import IsAuthenticatedOrReadOnly
# from form.models import *
# from form.admin import *


# Create your views here.
class StudentViewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    pagination_class=PageNumberPagination
    filter_backends=(filters.SearchFilter,filter.DjangoFilterBackend,)
    filterset_fields=('first_name',)
    search_fields=('first_name',)
