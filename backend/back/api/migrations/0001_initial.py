# Generated by Django 4.1.7 on 2023-12-12 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('price', models.IntegerField()),
                ('mileage', models.FloatField()),
                ('body_type', models.CharField(max_length=255)),
                ('transmission', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]