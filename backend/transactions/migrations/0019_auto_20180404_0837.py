# Generated by Django 2.0.3 on 2018-04-04 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0018_auto_20180402_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='wallet',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='transactions.Wallet', verbose_name='Wallet'),
            preserve_default=False,
        ),
    ]
