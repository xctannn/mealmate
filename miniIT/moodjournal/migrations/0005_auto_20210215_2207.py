# Generated by Django 3.1.5 on 2021-02-15 14:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moodjournal', '0004_auto_20210215_0041'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='moodcolor',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='energy',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='entry',
            name='happiness',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='entry',
            name='health',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='entry',
            name='hunger',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='entry',
            name='journal',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='entry',
            name='stress',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(10)]),
        ),
    ]
