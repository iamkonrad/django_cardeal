# Generated by Django 4.2.5 on 2023-09-23 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_car_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(choices=[('AUTOMATIC', 'AUTOMATIC'), ('MANUAL', 'MANUAL'), ('OTHER', 'OTHER')], max_length=200),
        ),
    ]
