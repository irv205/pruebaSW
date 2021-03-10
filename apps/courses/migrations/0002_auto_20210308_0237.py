# Generated by Django 3.1.6 on 2021-03-08 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='passing_score',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='answer',
            name='options',
            field=models.JSONField(),
        ),
    ]
