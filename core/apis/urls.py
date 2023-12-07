from django.urls import path, include
from apis.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"companies", CompanyViewsSet)
router.register(r"employees", EmployeeViewsSet)
urlpatterns = [path("", include(router.urls))]
