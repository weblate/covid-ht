# Generated by Django 3.1.5 on 2021-03-24 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0010_example_data_mark_as_finished'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='chtuid',
            field=models.CharField(blank=True, default='cHT00', max_length=5, verbose_name='Covid-HT Unique IDentifier'),
        ),
    ]