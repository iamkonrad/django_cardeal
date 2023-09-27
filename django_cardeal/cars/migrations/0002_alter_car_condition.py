# Generated by Django 4.2.5 on 2023-09-23 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='condition',
            field=models.CharField(choices=[('USED', 'USED'), ('NEW', 'NEW'), ('COLLISION', 'COLLISION'), ('PARTS', 'PARTS')], max_length=200),
        ),
    ]