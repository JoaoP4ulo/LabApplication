# Generated by Django 4.2.4 on 2023-08-07 17:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0003_alter_gettemperatura_hora_alter_settemperatura_hora"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gettemperatura",
            name="hora",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 8, 7, 14, 23, 28, 55537)
            ),
        ),
        migrations.AlterField(
            model_name="settemperatura",
            name="hora",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 8, 7, 14, 23, 28, 55537)
            ),
        ),
    ]
