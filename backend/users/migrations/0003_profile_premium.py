# Generated by Django 5.2 on 2025-04-28 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_old_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='premium',
            field=models.BooleanField(default=False),
        ),
    ]
