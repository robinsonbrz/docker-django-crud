# Generated by Django 3.2.19 on 2023-06-11 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('units', models.BigIntegerField()),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
            ],
        ),
    ]
