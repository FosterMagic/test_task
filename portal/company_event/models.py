from django.db import models
from django.contrib.auth.models import AbstractUser


class Company(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    address = models.CharField(max_length=150, blank=True, verbose_name='Адрес')
    postcode = models.IntegerField(default=197374, verbose_name='Почтовый индекс')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'


class Event(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    company = models.ForeignKey('Company', on_delete=models.PROTECT, null=True, verbose_name='Компания')
    image = models.ImageField(blank=True, upload_to='images', verbose_name='Изображение')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
