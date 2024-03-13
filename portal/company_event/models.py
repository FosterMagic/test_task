from django.db import models


# Create your models here.

class Company(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=150, blank=True)
    postcode = models.IntegerField(default=197374)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    company = models.ForeignKey('Company', on_delete=models.PROTECT, null=True)
    image = models.ImageField(blank=True, upload_to='images')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

