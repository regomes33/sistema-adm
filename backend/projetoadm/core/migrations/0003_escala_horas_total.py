# Generated by Django 4.0 on 2022-07-01 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_posto_escala_data_final_escala_data_inicio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='escala',
            name='horas_total',
            field=models.TimeField(null=True, verbose_name='horas'),
        ),
    ]
