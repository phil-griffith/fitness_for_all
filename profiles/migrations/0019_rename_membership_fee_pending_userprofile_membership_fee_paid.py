# Generated by Django 3.2.3 on 2021-07-24 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0018_userprofile_membership_fee_pending'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='membership_fee_pending',
            new_name='membership_fee_paid',
        ),
    ]
