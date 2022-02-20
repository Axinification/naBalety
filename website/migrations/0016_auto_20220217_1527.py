# Generated by Django 3.2.9 on 2022-02-17 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_event_is_promotor'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='pool_4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='pool_5',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='pool_6',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='pool_date_3',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='pool_date_4',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='pool_date_5',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='price_4',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='price_5',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='price_6',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='pool_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='pool_date_2',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='price_3',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]