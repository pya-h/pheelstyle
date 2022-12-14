# Generated by Django 3.2.12 on 2022-10-25 21:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=30, verbose_name='First Name')),
                ('lname', models.CharField(max_length=30, verbose_name='Last Name')),
                ('phone', models.CharField(max_length=11, unique=True, verbose_name='Phone Number')),
                ('email', models.CharField(max_length=100, unique=True, verbose_name='E-mail')),
                ('ip', models.CharField(blank=True, max_length=20, verbose_name='IP')),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('activated', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postal_code', models.CharField(max_length=10, verbose_name='Postal Code')),
                ('province', models.CharField(max_length=30, verbose_name='Province')),
                ('city', models.CharField(max_length=30, verbose_name='City')),
                ('address', models.CharField(max_length=256, verbose_name='Address')),
                ('avatar', models.ImageField(blank=True, upload_to='photos/avatars/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
