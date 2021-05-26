# Generated by Django 3.2.3 on 2021-05-19 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('LoanService', '0009_alter_emanet_given_source_barcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emanet',
            name='given_source_barcode',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AlterField(
            model_name='emanet',
            name='given_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]
