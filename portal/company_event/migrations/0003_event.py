# Generated by Django 5.0.3 on 2024-03-12 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_event', '0002_company_address_company_postcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]