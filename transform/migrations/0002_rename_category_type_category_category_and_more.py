# Generated by Django 4.2.5 on 2024-07-09 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transform', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_type',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='clubbed_name',
        ),
    ]
