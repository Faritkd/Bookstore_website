# Generated by Django 5.0.1 on 2024-02-24 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_book_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('special_status', 'can read all books')]},
        ),
    ]
