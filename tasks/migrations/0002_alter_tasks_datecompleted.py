# Generated by Django 4.1.2 on 2022-10-27 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='dateCompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]