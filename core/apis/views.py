from django.shortcuts import render
from rest_framework import viewsets
from apis.models import *
from apis.serializers import *


# Create your views here.
class CompanyViewsSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = Company_serializers
