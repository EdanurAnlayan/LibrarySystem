# Generated by Django 3.1.3 on 2021-06-05 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoanService', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emanet',
            name='given_user_number',
            field=models.CharField(default='030716003', max_length=11),
            preserve_default=False,
        ),
    ]
