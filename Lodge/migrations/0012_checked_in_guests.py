# Generated by Django 4.0.1 on 2022-02-05 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Lodge', '0011_checkin_customer_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checked_in_guests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Lodge.booking')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Lodge.customer')),
            ],
        ),
    ]
