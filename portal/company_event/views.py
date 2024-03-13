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



def index(request):
    return HttpResponse("<center><h1>Тестовое задание: стартовая страница</h1>\
    <br><a href='http://127.0.0.1:8000/admin/'>Админка</a> \
     <br><a href='http://127.0.0.1:8000/api/v1/token'>Получить JWT токены</a> \
    <br><a href='http://127.0.0.1:8000/api/v1/companies'>Организации</a> \
    <br><a href='http://127.0.0.1:8000/api/v1/events'>Мероприятия</a> \
    <br><a href='http://127.0.0.1:8000/api/v1/event_details/1/'>Изменить мероприятие</a> \
    <br><a href='http://127.0.0.1:8000/api/v1/companies_details/2/'>Изменить организацию</a> \
    <br><h1><i>Доступ в админку как по логину, так и по e-mail.</i> Пользователь: <u>root</u>. E-mail: <u>root@mail.ru</u>. \
     Пароль: <u>12345</u></h1></center>"
                        )

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
