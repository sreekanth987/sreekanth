# Generated by Django 5.0.6 on 2024-06-26 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp_app', '0029_booked_bookingstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='newevent',
            name='fullamount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
