# Generated by Django 4.2.16 on 2024-10-24 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_name', models.CharField(max_length=100)),
                ('bus_number', models.CharField(max_length=100)),
                ('bus_capacity', models.IntegerField()),
                ('days_of_operation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_name', models.CharField(max_length=100)),
                ('route_from', models.CharField(max_length=100)),
                ('route_to', models.CharField(max_length=100)),
                ('route_price', models.IntegerField()),
                ('route_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.IntegerField()),
                ('seat_status', models.BooleanField(default=False)),
                ('bus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.bus')),
            ],
        ),
        migrations.AddField(
            model_name='bus',
            name='bus_route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.route'),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField(auto_now_add=True)),
                ('booking_time', models.TimeField(auto_now_add=True)),
                ('booking_status', models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')], max_length=100)),
                ('booking_price', models.IntegerField()),
                ('booking_email', models.EmailField(max_length=100)),
                ('booking_phone', models.CharField(max_length=15)),
                ('bus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.bus')),
                ('seat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.seat')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddIndex(
            model_name='seat',
            index=models.Index(fields=['seat_number', 'bus_id'], name='booking_sea_seat_nu_ec4174_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='seat',
            unique_together={('seat_number', 'bus_id')},
        ),
    ]
