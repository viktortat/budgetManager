# Generated by Django 2.0.3 on 2018-05-05 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0023_budget_period'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budget',
            name='category',
        ),
        migrations.AddField(
            model_name='budget',
            name='categories',
            field=models.ManyToManyField(related_name='budgets', to='transactions.Category', verbose_name='Categories'),
        ),
    ]
