# Generated by Django 4.0.1 on 2022-02-04 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lodge', '0005_alter_checkin_checkin_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='first_date',
            field=models.CharField(max_length=240),
        ),
        migrations.AlterField(
            model_name='booking',
            name='last_date',
            field=models.CharField(max_length=240),
        ),
    ]
