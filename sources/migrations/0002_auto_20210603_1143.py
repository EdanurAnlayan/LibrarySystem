# Generated by Django 3.1.3 on 2021-06-03 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sources',
            name='barcode',
            field=models.CharField(editable=False, max_length=11, unique=True),
        ),
    ]
