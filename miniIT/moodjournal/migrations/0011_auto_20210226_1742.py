# Generated by Django 3.1.4 on 2021-02-26 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moodjournal', '0010_auto_20210225_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='author',
            field=models.CharField(default='Anonymous', max_length=15),
        ),
    ]