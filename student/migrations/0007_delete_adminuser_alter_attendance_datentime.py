# Generated by Django 4.1.1 on 2022-09-30 08:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_alter_attendance_datentime'),
    ]

    operations = [
        migrations.DeleteModel(
            name='adminuser',
        ),
        migrations.AlterField(
            model_name='attendance',
            name='datentime',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 30, 14, 17, 0, 316844)),
        ),
    ]
