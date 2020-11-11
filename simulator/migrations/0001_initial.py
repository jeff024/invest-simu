# Generated by Django 3.1.3 on 2020-11-11 05:13

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
            name='Stock',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WatchListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulator.stock')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WatchListAlert',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('watchprice', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('triggered', models.BooleanField(default=False)),
                ('shown', models.BooleanField(default=False)),
                ('dateTriggered', models.CharField(max_length=40)),
                ('action', models.CharField(default='buy', max_length=4)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulator.stock')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('dateTriggered',),
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('units', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('date', models.CharField(max_length=30)),
                ('action', models.CharField(max_length=30)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulator.stock')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('dateBought', models.CharField(max_length=30)),
                ('orignialUnitBought', models.PositiveIntegerField()),
                ('unitSold', models.PositiveIntegerField()),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulator.stock')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, default=10000, max_digits=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
