# Generated by Django 5.0.1 on 2024-02-05 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_rename_auther_books_author'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
    ]
