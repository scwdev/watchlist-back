# Generated by Django 3.2.7 on 2021-09-09 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgurl', models.URLField(blank=True)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('runtime', models.CharField(blank=True, max_length=50)),
                ('medium', models.CharField(blank=True, max_length=100)),
                ('genre', models.CharField(blank=True, max_length=100)),
                ('source', models.CharField(blank=True, max_length=100)),
                ('watched', models.BooleanField(default=False)),
                ('notes', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
