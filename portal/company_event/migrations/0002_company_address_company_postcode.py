# Generated by Django 5.0.3 on 2024-03-12 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='company',
            name='postcode',
            field=models.IntegerField(default=197374),
        ),
    ]