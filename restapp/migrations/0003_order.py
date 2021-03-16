# Generated by Django 3.1.7 on 2021-03-10 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0002_item_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('order_no', models.CharField(max_length=10)),
                ('details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_details', to='restapp.item')),
            ],
        ),
    ]
