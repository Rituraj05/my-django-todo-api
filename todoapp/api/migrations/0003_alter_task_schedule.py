# Generated by Django 4.1.1 on 2022-09-24 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_task_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='schedule',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]