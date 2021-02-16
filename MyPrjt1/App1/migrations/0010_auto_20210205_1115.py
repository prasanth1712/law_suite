# Generated by Django 3.0.3 on 2021-02-05 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0009_auto_20210205_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='account_number',
            field=models.IntegerField(unique=True),
        ),
        migrations.AddConstraint(
            model_name='bank',
            constraint=models.CheckConstraint(check=models.Q(rtgs_number__gt=0), name='rtgs_number'),
        ),
        migrations.AddConstraint(
            model_name='bank',
            constraint=models.CheckConstraint(check=models.Q(rtgs_number__gt=0), name='account_number'),
        ),
    ]