# Generated by Django 5.0.6 on 2024-05-27 02:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('receiver_name', models.CharField(max_length=255)),
                ('receiver_phone', models.CharField(max_length=15)),
                ('receiver_address', models.CharField(max_length=255)),
                ('is_ordered', models.BooleanField(default=False)),
                ('is_paid', models.BooleanField(default=False)),
                ('total', models.FloatField(default=0)),
                ('description', models.CharField(max_length=512)),
                ('payment_id', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('price', models.FloatField()),
                ('discount', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]