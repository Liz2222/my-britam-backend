# Generated by Django 4.2.2 on 2023-06-29 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brit_users', '0014_users_available_points_users_loyalty_points_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
