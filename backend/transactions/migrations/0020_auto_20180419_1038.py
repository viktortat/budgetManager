# Generated by Django 2.0.3 on 2018-04-19 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0019_auto_20180404_0837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Amount')),
                ('categories', models.ManyToManyField(related_name='budgets', to='transactions.Category', verbose_name='Categories')),
            ],
        ),
        migrations.AlterField(
            model_name='wallet',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_wallets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='shared_wallets', to=settings.AUTH_USER_MODEL, verbose_name='Users'),
        ),
    ]