# Generated by Django 3.2.5 on 2021-07-21 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('category_name', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
                ('category_image', models.CharField(max_length=255)),
            ],
        ),
    ]
