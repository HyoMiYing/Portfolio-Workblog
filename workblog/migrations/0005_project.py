# Generated by Django 2.2.2 on 2019-09-15 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workblog', '0004_auto_20190916_0046'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('github_url', models.CharField(max_length=100)),
                ('site_url', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
