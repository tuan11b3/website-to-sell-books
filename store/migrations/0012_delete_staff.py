# Generated by Django 4.1.7 on 2023-03-06 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_rename_name_staff_fullname_staff_date_joined_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Staff',
        ),
    ]
