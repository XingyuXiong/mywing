# Generated by Django 2.1.7 on 2019-04-01 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20190401_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='dstLongitude',
            field=models.FloatField(blank=True, default=None, editable=False, null=True),
        ),
    ]
