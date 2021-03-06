# Generated by Django 3.1.5 on 2021-01-28 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SortFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mealtype', models.CharField(max_length=100)),
                ('calories', models.IntegerField()),
                ('carbs', models.IntegerField()),
                ('protein', models.IntegerField()),
                ('fat', models.IntegerField()),
                ('fibre', models.IntegerField()),
                ('size', models.IntegerField()),
            ],
        ),
    ]
