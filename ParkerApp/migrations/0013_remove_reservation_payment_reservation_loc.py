# Generated by Django 4.2.5 on 2024-05-10 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ParkerApp', '0012_alter_reservation_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='payment',
        ),
        migrations.AddField(
            model_name='reservation',
            name='loc',
            field=models.CharField(choices=[('Idukki', 'Idukki'), ('Ernakulam', 'Ernakulam'), ('Trivandrum', 'Trivandrum'), ('Chennai', 'Chennai')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]
