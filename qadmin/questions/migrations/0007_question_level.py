# Generated by Django 3.0.3 on 2020-02-06 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_auto_20200206_0220'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='level',
            field=models.IntegerField(choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Hard')], default=1),
        ),
    ]
