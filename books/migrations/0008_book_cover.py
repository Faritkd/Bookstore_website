# Generated by Django 5.0.1 on 2024-02-23 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_review_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers/'),
        ),
    ]
