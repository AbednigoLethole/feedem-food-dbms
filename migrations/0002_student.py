# Generated by Django 3.1.6 on 2021-02-17 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('studentNo', models.IntegerField(max_length=7)),
                ('mealPlan', models.CharField(max_length=3)),
                ('jan', models.BooleanField(default=False)),
                ('feb', models.BooleanField(default=False)),
                ('mar', models.BooleanField(default=False)),
                ('apr', models.BooleanField(default=False)),
                ('may', models.BooleanField(default=False)),
                ('jun', models.BooleanField(default=False)),
                ('jul', models.BooleanField(default=False)),
                ('sep', models.BooleanField(default=False)),
                ('octo', models.BooleanField(default=False)),
                ('nov', models.BooleanField(default=False)),
                ('dec', models.BooleanField(default=False)),
            ],
        ),
    ]