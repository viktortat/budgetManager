# Generated by Django 2.0.3 on 2018-03-28 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0004_auto_20180328_0813'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set(),
        ),
    ]
