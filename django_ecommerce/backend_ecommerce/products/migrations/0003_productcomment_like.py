# Generated by Django 5.0.6 on 2024-05-27 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcomment',
            name='like',
            field=models.IntegerField(null=True),
        ),
    ]