# Generated by Django 5.0.6 on 2024-06-19 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mp_app', '0007_rename_book_booked'),
    ]

    operations = [
        migrations.DeleteModel(
            name='booked',
        ),
    ]
