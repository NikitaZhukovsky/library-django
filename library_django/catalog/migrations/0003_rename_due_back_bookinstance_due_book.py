# Generated by Django 5.0.3 on 2024-03-17 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_country_options_alter_author_date_of_birth_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinstance',
            old_name='due_back',
            new_name='due_book',
        ),
    ]
