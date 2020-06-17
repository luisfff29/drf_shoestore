# Generated by Django 3.0.7 on 2020-06-17 16:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ShoeColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(choices=[('red', 'Red'), ('orange', 'Orange'), ('yellow', 'Yellow'), ('green', 'Green'), ('blue', 'Blue'), ('indigo', 'Indigo'), ('violet', 'Violet'), ('white', 'White'), ('black', 'Black')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ShoeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(choices=[('sneaker', 'Sneaker'), ('boot', 'Boot'), ('sandal', 'Sandal'), ('dress', 'Dress'), ('other', 'Other')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.PositiveIntegerField(help_text='Max shoe size is 22', validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(22)])),
                ('brand', models.CharField(max_length=200)),
                ('material', models.CharField(max_length=200)),
                ('fasten_type', models.CharField(max_length=200)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoe_store.ShoeColor')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoe_store.Manufacturer')),
                ('shoe_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoe_store.ShoeType')),
            ],
        ),
    ]
