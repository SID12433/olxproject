# Generated by Django 4.2.5 on 2023-10-06 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('remainder', '0003_alter_vehicles_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicles',
            old_name='owner',
            new_name='user',
        ),
    ]
