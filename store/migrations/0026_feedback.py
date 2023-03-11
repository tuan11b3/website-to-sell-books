# Generated by Django 4.1.7 on 2023-03-11 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_alter_customer_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField()),
                ('happy', models.BooleanField()),
                ('responded', models.BooleanField()),
                ('custom_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.customer')),
                ('staff_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.staff')),
            ],
        ),
    ]