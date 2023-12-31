# Generated by Django 4.1.9 on 2023-06-16 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0016_etalon"),
    ]

    operations = [
        migrations.CreateModel(
            name="ChemicalsRecip",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "protein",
                    models.FloatField(default=0, verbose_name="Массовая доля белка, %"),
                ),
                (
                    "fat",
                    models.FloatField(default=0, verbose_name="Массовая доля жира, %"),
                ),
                (
                    "carbohydrates",
                    models.FloatField(
                        default=0, verbose_name="Массовая доля углевода, %"
                    ),
                ),
                ("kkal", models.FloatField(default=0, verbose_name="ккал")),
                ("kJ", models.FloatField(default=0, verbose_name="кДж")),
                (
                    "recip",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="main.recips",
                    ),
                ),
            ],
            options={
                "verbose_name": " -- (Химический состав) -- ",
            },
        ),
        migrations.CreateModel(
            name="AminoAcidCompositionRecip",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("izoleitsin", models.FloatField(default=0, verbose_name="Изолейцин")),
                ("leitsin", models.FloatField(default=0, verbose_name="Лейцин")),
                ("lisin", models.FloatField(default=0, verbose_name="Лизин")),
                ("valin", models.FloatField(default=0, verbose_name="Валин")),
                (
                    "metilcistein",
                    models.FloatField(default=0, verbose_name="Метилцистеин"),
                ),
                (
                    "feniltirosin",
                    models.FloatField(default=0, verbose_name="Фенилтиросин"),
                ),
                ("triptofan", models.FloatField(default=0, verbose_name="Триптофан")),
                ("treon", models.FloatField(default=0, verbose_name="Треон")),
                (
                    "recip",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="main.recips",
                    ),
                ),
            ],
            options={
                "verbose_name": " -- (Аминокислотный Состав) -- ",
            },
        ),
    ]
