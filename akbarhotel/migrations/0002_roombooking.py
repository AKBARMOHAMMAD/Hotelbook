# Generated by Django 2.1.4 on 2018-12-14 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akbarhotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type', models.CharField(max_length=20)),
                ('available_rooms', models.IntegerField()),
                ('Check_in', models.DateField()),
                ('Check_out', models.DateField()),
            ],
        ),
    ]
