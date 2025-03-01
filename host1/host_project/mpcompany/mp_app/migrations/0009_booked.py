# Generated by Django 5.0.6 on 2024-06-19 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp_app', '0008_delete_booked'),
    ]

    operations = [
        migrations.CreateModel(
            name='booked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clintname', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('eventname', models.CharField(max_length=100)),
                ('date_from', models.DateField(default='2024-01-01')),
                ('date_to', models.DateField(default='2024-01-01')),
                ('others', models.CharField(max_length=100)),
            ],
        ),
    ]
