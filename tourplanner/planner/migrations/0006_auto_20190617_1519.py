# Generated by Django 2.2.1 on 2019-06-17 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0005_auto_20190614_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='Email',
            field=models.EmailField(max_length=50),
        ),
    ]
