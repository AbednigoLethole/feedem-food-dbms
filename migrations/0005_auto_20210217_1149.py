# Generated by Django 3.1.6 on 2021-02-17 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodApp', '0004_auto_20210217_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='mealPlan',
            field=models.CharField(max_length=4),
        ),
    ]
