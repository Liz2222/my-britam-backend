# Generated by Django 4.2.2 on 2023-06-28 11:24

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('brit_users', '0011_transaction_mpesa_receipt_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', ckeditor.fields.RichTextField()),
                ('video', embed_video.fields.EmbedVideoField(blank=True)),
                ('author', models.CharField(max_length=100)),
                ('publication_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='LoyaltyPoints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brit_users.users')),
            ],
        ),
    ]