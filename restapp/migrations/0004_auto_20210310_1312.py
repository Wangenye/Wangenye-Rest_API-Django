# Generated by Django 3.1.7 on 2021-03-10 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0003_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_no',
            field=models.CharField(default='HY122LY1', max_length=10),
        ),
    ]
