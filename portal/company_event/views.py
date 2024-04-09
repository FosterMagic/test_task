from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .models import Company, Event
from .serializers import CompanySerializer, EventSerializer


class UniversalPaginationStyle(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100

# Create your views here.
class CompanyAPIVIew(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = UniversalPaginationStyle


class CompanyAPIUpdate(generics.UpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = UniversalPaginationStyle


class CompanyAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = UniversalPaginationStyle


class EventAPIVIew(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = UniversalPaginationStyle


class EventAPIUpdate(generics.UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = UniversalPaginationStyle


class EventAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = UniversalPaginationStyle


menu = ['О сайте', 'Добавить мероприятие', 'Обратная связь', 'Войти']


def index(request):
    posts = Event.objects.all()
    return render(request, 'company_event/main_menu.html', {'title': 'Main project page'})

def about(request):
    return render(request, 'company_event/about.html', {'menu': menu, 'title': 'About this project'})


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
