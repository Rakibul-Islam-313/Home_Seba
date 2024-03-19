# Generated by Django 4.2.7 on 2024-01-25 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=40)),
                ('service_detail', models.TextField()),
                ('service_price', models.IntegerField()),
            ],
        ),
    ]
