from django.contrib import admin
from django.urls import path, include
from companyapis.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("test/", test, name="test"),
    path("api/v1/", include("apis.urls")),
]
