# Generated by Django 4.2.3 on 2023-08-20 17:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserAdress',
            new_name='UserAddress',
        ),
        migrations.RenameField(
            model_name='userbankaccount',
            old_name='initial_deposit_date',
            new_name='initial_deposite_date',
        ),
    ]
