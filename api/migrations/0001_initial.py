# Generated by Django 3.2.9 on 2021-11-24 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('isbn', models.TextField()),
                ('year', models.IntegerField()),
                ('country', models.TextField()),
                ('number_of_pages', models.IntegerField()),
                ('publisher', models.TextField()),
                ('release_date', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('books', models.ManyToManyField(to='api.items')),
            ],
        ),
    ]