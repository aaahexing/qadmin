# Generated by Django 3.0.3 on 2020-02-06 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_auto_20200206_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='references',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='supplement',
            field=models.TextField(blank=True),
        ),
    ]