# Generated by Django 5.1.1 on 2024-10-12 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_guestorder'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GuestOrder',
        ),
    ]
