# Generated by Django 2.2.5 on 2019-09-28 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0002_auto_20190926_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='content_long',
            field=models.CharField(max_length=3000),
        ),
    ]
