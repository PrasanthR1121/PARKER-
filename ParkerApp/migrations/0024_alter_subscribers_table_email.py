# Generated by Django 4.2.5 on 2024-07-01 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ParkerApp', '0023_alter_subscribers_table_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribers_table',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
