# Generated by Django 3.1.7 on 2021-03-16 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0013_auto_20210316_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_no',
            field=models.CharField(default='715B347O', max_length=10),
        ),
    ]
