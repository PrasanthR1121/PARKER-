# Generated by Django 4.2.5 on 2024-06-11 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ParkerApp', '0018_rename_slots_slots_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
