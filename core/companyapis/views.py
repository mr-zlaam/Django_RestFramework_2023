from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def test(request):
    friends = ["zlaam", "siraj", "khan", "darkness"]
    return JsonResponse(friends, safe=False)
