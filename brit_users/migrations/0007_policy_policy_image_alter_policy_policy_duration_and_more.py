# Generated by Django 4.2.2 on 2023-06-24 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brit_users', '0006_users_referral_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='policy',
            name='policy_image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='policy',
            name='policy_duration',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='policy',
            name='policy_status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
