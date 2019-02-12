# Generated by Django 2.1.5 on 2019-02-11 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Angel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=16)),
                ('central_key', models.CharField(max_length=64)),
                ('distribution', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='LoginItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.UUIDField()),
                ('angel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='angel.Angel')),
            ],
        ),
    ]