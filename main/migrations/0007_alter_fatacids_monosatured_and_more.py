# Generated by Django 4.1.9 on 2023-06-05 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0006_remove_products_categiry_products_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fatacids",
            name="monosatured",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="main.monosaturated",
            ),
        ),
        migrations.AlterField(
            model_name="fatacids",
            name="polyunsaturated",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="main.polyunsaturated",
            ),
        ),
        migrations.AlterField(
            model_name="fatacids",
            name="product",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="main.products",
            ),
        ),
        migrations.AlterField(
            model_name="fatacids",
            name="satured",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="main.saturatedfats",
            ),
        ),
    ]
