# Generated by Django 2.0.3 on 2018-03-08 00:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('short_url', models.SlugField(max_length=200, unique=True)),
                ('actual_url', models.URLField()),
                ('last_visited', models.DateTimeField(auto_now=True)),
                ('visit_count', models.IntegerField(default=0)),
            ],
        ),
    ]