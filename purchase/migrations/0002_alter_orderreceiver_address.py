# Generated by Django 3.2.12 on 2022-10-26 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderreceiver',
            name='address',
            field=models.TextField(max_length=256, verbose_name='Address'),
        ),
    ]