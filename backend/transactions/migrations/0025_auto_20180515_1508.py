# Generated by Django 2.0.3 on 2018-05-15 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0024_auto_20180505_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='color',
            field=models.CharField(max_length=32, verbose_name='Color'),
        ),
    ]
