# Generated by Django 3.1.5 on 2021-02-05 20:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_add_hemogramfields_alter_names_and_validators'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='baso_Upercentage_Rwbc',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Basophil Granulocytes (% of White Blood Cells)', max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(99.0)], verbose_name='BASO (% WBC)'),
        ),
        migrations.AlterField(
            model_name='data',
            name='eo_Upercentage_Rwbc',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Eosinophil Granulocytes (% of White Blood Cells)', max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(99.0)], verbose_name='EO (% WBC)'),
        ),
        migrations.AlterField(
            model_name='data',
            name='neut_Upercentage_Rwbc',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Neutrophil Granulocytes (% of White Blood Cells)', max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(0.01), django.core.validators.MaxValueValidator(99.0)], verbose_name='NEUT (% WBC)'),
        ),
    ]
