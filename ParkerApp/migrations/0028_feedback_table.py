# Generated by Django 5.0.6 on 2024-07-19 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ParkerApp', '0027_subscribers_table_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.TextField(max_length=50)),
                ('rating', models.CharField(max_length=1)),
            ],
        ),
    ]
