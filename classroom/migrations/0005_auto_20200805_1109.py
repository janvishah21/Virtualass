# Generated by Django 2.2.12 on 2020-08-05 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0004_auto_20200804_2218'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='message',
            unique_together=set(),
        ),
    ]
