# Generated by Django 3.2.4 on 2021-06-28 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosp_app', '0007_auto_20210617_1214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='dept',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='doc',
            new_name='doctor',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='mob_no',
            new_name='mobile_no',
        ),
    ]
