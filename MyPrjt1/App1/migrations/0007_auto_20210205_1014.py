# Generated by Django 3.0.3 on 2021-02-05 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0006_auto_20210204_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='bank_name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
