# Generated by Django 4.2.2 on 2023-06-07 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_new',
            field=models.BooleanField(default=True),
        ),
    ]
