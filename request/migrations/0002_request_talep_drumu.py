# Generated by Django 3.1.3 on 2021-05-28 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='talep_drumu',
            field=models.BooleanField(default=False),
        ),
    ]