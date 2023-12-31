# Generated by Django 4.1.9 on 2023-06-24 13:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0020_recips_date_analis"),
    ]

    operations = [
        migrations.AddField(
            model_name="aminoacidcompositionrecip",
            name="c_min",
            field=models.FloatField(default=0, verbose_name="Cmin"),
        ),
        migrations.AddField(
            model_name="aminoacidcompositionrecip",
            name="feniltirosin1",
            field=models.FloatField(default=0, verbose_name="Фенилтиросин C, %"),
        ),
        migrations.AddField(
            model_name="aminoacidcompositionrecip",
            name="feniltirosin_a",
            field=models.FloatField(default=0, verbose_name="Фенилтиросин a, %"),
        ),
        migrations.AddField(
            model_name="aminoacidcompositionrecip",
            name="izoleitsin1",
            field=models.FloatField(default=0, verbose_name="Изолейцин C, %"),
        ),
        migrations.AddField(
            model_name="aminoacidcompositionrecip",
            name="izoleitsin_a",
            field=models.FloatField(default=0, verbose_name="Изолейцин a, %"),
        ),
        migrations.AddField(
            model_name="aminoacidcompositionrecip",
            name="leitsin1",
            field=models.FloatField(default=0, verbose_name="Лейцин C, %"),
        ),
        migrations.AddField(
            model_name="aminoacidcompositionrecip",
            name="leitsin_a",
            field=models.FloatField(default=0, verbose_name="Лейцин a, %"),
        ),
        migrations.AddField(
            model_name="aminoacidcompositionrecip",
            name="lisin1",
            field=models.FloatField(default=0, verbose_name="Лизин C, %"),
        ),
        migrations.AddField(
            model_name="aminoacidcompositionrecip",
            name="lisin_a",
            field=models.FloatField(default=0, verbose_name="Лизин a, %"),
        ),
        migrations.AddField(
            model_name="aminoacidcompositionrecip",
            name="metilcistein1",
            field=models.FloatField(default=0, verbose_name="Метилцистеин C, %"),
        ),
        migrations.AddField(
            model_name="aminoacidcompositionrecip",
            name="metilcistein_a",
            field=models.FloatField(default=0, verbose_name="Метилцистеин a, %"),
        ),
        migrations.AddField(
            model_name="aminoacidcompositionrecip",
            name="treon1",
            field=models.FloatField(default=0, verbose_name="Треон C, %"),
        ),
        migrations.AddField(
            model_name="aminoacidcompositionrecip",
            name="treon_a",
            field=models.FloatField(default=0, verbose_name="Треон a, %"),
        ),
        migrations.AddField(
            model_name="aminoacidcompositionrecip",
            name="triptofan1",
            field=models.FloatField(default=0, verbose_name="Триптофан C, %"),
        ),
        migrations.AddField(
            model_name="aminoacidcompositionrecip",
            name="triptofan_a",
            field=models.FloatField(default=0, verbose_name="Триптофан a, %"),
        ),
        migrations.AddField(
            model_name="aminoacidcompositionrecip",
            name="valin1",
            field=models.FloatField(default=0, verbose_name="Валин C, %"),
        ),
        migrations.AddField(
            model_name="aminoacidcompositionrecip",
            name="valin_a",
            field=models.FloatField(default=0, verbose_name="Валин a, %"),
        ),
    ]
