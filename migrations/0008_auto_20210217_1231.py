# Generated by Django 3.1.6 on 2021-02-17 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodApp', '0007_student_aug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='studentNo',
            field=models.IntegerField(default=0),
        ),
    ]