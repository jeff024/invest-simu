# Generated by Django 3.1.2 on 2020-10-28 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlistitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]