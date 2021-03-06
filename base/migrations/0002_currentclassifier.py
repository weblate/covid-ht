# Generated by Django 3.1.5 on 2021-01-15 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supervised_learning', '0001_initial'),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentClassifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classifier', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='current_classifier', to='supervised_learning.hgbtreeclassifier')),
            ],
            options={
                'verbose_name': 'Current Classifier',
            },
        ),
    ]
