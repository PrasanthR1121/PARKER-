# Generated by Django 5.0.6 on 2024-07-20 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ParkerApp', '0035_alter_feedback_table_email_alter_feedback_table_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback_table',
            name='email',
            field=models.EmailField(default='Email@gmail.com', max_length=254),
        ),
    ]
