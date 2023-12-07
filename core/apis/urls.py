from django.urls import path, include
from apis.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"Companies", CompanyViewsSet)
urlpatterns = [path("", include(router.urls))]
