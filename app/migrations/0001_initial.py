# Generated by Django 3.1.1 on 2020-09-10 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.BigIntegerField(blank=True, primary_key=True, serialize=False)),
                ('exact_url', models.URLField()),
                ('hash_slug', models.CharField(blank=True, max_length=6)),
            ],
        ),
    ]
