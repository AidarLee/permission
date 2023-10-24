# Generated by Django 4.1.9 on 2023-06-05 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_etalon"),
    ]

    operations = [
        migrations.CreateModel(
            name="Monosaturated",
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
                    "value",
                    models.FloatField(
                        default=0, verbose_name="Значение Ненасыщенной жирнокислоты"
                    ),
                ),
                (
                    "Myristoleic",
                    models.FloatField(default=0, verbose_name="С14:1 Миристолеиновая"),
                ),
                (
                    "Pentadecene",
                    models.FloatField(default=0, verbose_name="С15:1 Пентадеценовая"),
                ),
                (
                    "Pamlmitoleic",
                    models.FloatField(
                        default=0, verbose_name="С16:1 Памльмитолеиновая"
                    ),
                ),
                (
                    "MargarineOleic",
                    models.FloatField(
                        default=0, verbose_name="С17:1 Маргаринолеиновая"
                    ),
                ),
                ("Oleic", models.FloatField(default=0, verbose_name="С18:1 Олеиновая")),
                (
                    "Eicosene",
                    models.FloatField(default=0, verbose_name="С20:1 Эйкозеновая"),
                ),
                (
                    "Selaholeva",
                    models.FloatField(default=0, verbose_name="С24:1 Селахолевая"),
                ),
            ],
            options={
                "verbose_name": " -- ( Ненасыщенная жирнокислота ) -- ",
            },
        ),
        migrations.CreateModel(
            name="Polyunsaturated",
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
                    "value",
                    models.FloatField(
                        default=0, verbose_name="Значение Полиненасыщенной жирнокислоты"
                    ),
                ),
                (
                    "Linoleic",
                    models.FloatField(default=0, verbose_name="С18:2n6c Линолевая"),
                ),
                (
                    "Linoleidine",
                    models.FloatField(
                        default=0, verbose_name="С18:2n6t Линолеидиновая"
                    ),
                ),
                (
                    "Y_Linolenic",
                    models.FloatField(default=0, verbose_name="С18:3n6 Y-Линоленовая"),
                ),
                (
                    "Linolenic",
                    models.FloatField(default=0, verbose_name="С18:3n3 Линоленовая"),
                ),
                (
                    "Eicosatriene",
                    models.FloatField(
                        default=0,
                        verbose_name="С20:3n6c (cis-8, 11, 14) Эйкозатриеновая",
                    ),
                ),
            ],
            options={
                "verbose_name": " -- ( Полиненасыщенная жирнокислота ) -- ",
            },
        ),
        migrations.CreateModel(
            name="SaturatedFats",
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
                    "value",
                    models.FloatField(
                        default=0, verbose_name="Значение Насыщенной жирнокислоты"
                    ),
                ),
                (
                    "Caprylic",
                    models.FloatField(default=0, verbose_name="С8:0 Каприловая"),
                ),
                (
                    "Сapric",
                    models.FloatField(default=0, verbose_name="С10:0 Каприновая"),
                ),
                (
                    "Undecane",
                    models.FloatField(default=0, verbose_name="С11:0 Ундекановая"),
                ),
                (
                    "Lauric",
                    models.FloatField(default=0, verbose_name="С12:0 Лауриновая"),
                ),
                (
                    "Tridecanoic",
                    models.FloatField(default=0, verbose_name="С13:0 Тридекановая"),
                ),
                (
                    "Myristic",
                    models.FloatField(default=0, verbose_name="С14:0 Миристиновая"),
                ),
                (
                    "Pentadecanoic",
                    models.FloatField(default=0, verbose_name="С15:0 Пентадекановая"),
                ),
                (
                    "Palmitic",
                    models.FloatField(default=0, verbose_name="С16:0 Пальмитиновая"),
                ),
                (
                    "Margarine",
                    models.FloatField(default=0, verbose_name="С17:0 Маргариновая"),
                ),
                (
                    "Stearic",
                    models.FloatField(default=0, verbose_name="С18:0 Стеариновая"),
                ),
                (
                    "Arachinoic",
                    models.FloatField(default=0, verbose_name="С20:0 Арахиновая"),
                ),
                (
                    "Geneicasonic",
                    models.FloatField(default=0, verbose_name="С21:0 Генейказоновая"),
                ),
                (
                    "Begenovaya",
                    models.FloatField(default=0, verbose_name="С22:0 Бегеновая"),
                ),
                (
                    "Tricosane",
                    models.FloatField(default=0, verbose_name="С23:0 Трикозановая"),
                ),
            ],
            options={
                "verbose_name": " -- ( Насыщенная жирнокислота ) -- ",
            },
        ),
        migrations.RemoveField(
            model_name="chemicalsingredients",
            name="ingredient",
        ),
        migrations.RemoveField(
            model_name="etalon",
            name="product",
        ),
        migrations.RemoveField(
            model_name="fatacidsingredients",
            name="ingredient",
        ),
        migrations.RemoveField(
            model_name="ingredients",
            name="category",
        ),
        migrations.RemoveField(
            model_name="mineralsingredients",
            name="ingredient",
        ),
        migrations.RemoveField(
            model_name="fatacids",
            name="type_of_acid",
        ),
        migrations.RemoveField(
            model_name="fatacids",
            name="value",
        ),
        migrations.AlterField(
            model_name="types",
            name="Name_of_type",
            field=models.CharField(
                help_text="(Продукт, Ингредиент, Эталонный продукт и т.д.)",
                max_length=75,
                null=True,
                verbose_name="Наименование типа",
            ),
        ),
        migrations.DeleteModel(
            name="AminoAcidCompOfIng",
        ),
        migrations.DeleteModel(
            name="ChemicalsIngredients",
        ),
        migrations.DeleteModel(
            name="Etalon",
        ),
        migrations.DeleteModel(
            name="FatAcidsIngredients",
        ),
        migrations.DeleteModel(
            name="Ingredients",
        ),
        migrations.DeleteModel(
            name="MineralsIngredients",
        ),
        migrations.AddField(
            model_name="fatacids",
            name="monosatured",
            field=models.ForeignKey(
                default="1",
                on_delete=django.db.models.deletion.RESTRICT,
                to="main.monosaturated",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="fatacids",
            name="polyunsaturated",
            field=models.ForeignKey(
                default="1",
                on_delete=django.db.models.deletion.RESTRICT,
                to="main.polyunsaturated",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="fatacids",
            name="satured",
            field=models.ForeignKey(
                default="1",
                on_delete=django.db.models.deletion.RESTRICT,
                to="main.saturatedfats",
            ),
            preserve_default=False,
        ),
    ]