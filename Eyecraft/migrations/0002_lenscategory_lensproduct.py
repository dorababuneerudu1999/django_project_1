# Generated by Django 5.1.5 on 2025-01-15 17:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eyecraft', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LensCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=200)),
                ('categoryDesc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LensProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=200)),
                ('productDesc', models.TextField()),
                ('productPrice', models.DecimalField(decimal_places=2, max_digits=7)),
                ('productImage', models.ImageField(upload_to='products/images/')),
                ('productRating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('productCategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Eyecraft.lenscategory')),
            ],
        ),
    ]
