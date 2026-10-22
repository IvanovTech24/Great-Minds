from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def home_page_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'core/home-page.html')