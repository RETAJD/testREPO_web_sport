# Generated by Django 3.1.4 on 2020-12-22 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]