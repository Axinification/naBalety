# Generated by Django 3.2.9 on 2022-03-13 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_auto_20220312_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='banner',
            field=models.ImageField(default='banners/logo-wersja-pełna.png', upload_to='banners/'),
        ),
    ]