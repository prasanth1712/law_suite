# Generated by Django 3.0.3 on 2021-02-01 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0002_auto_20210201_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='bank',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App1.Bank'),
        ),
    ]