# Generated by Django 2.0.3 on 2018-04-23 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0021_auto_20180419_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='wallet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='transactions.Wallet', verbose_name='Wallet'),
        ),
    ]
