# Generated by Django 4.0 on 2022-01-16 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='link1',
            field=models.URLField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='link2',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
