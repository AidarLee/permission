# Generated by Django 4.1.9 on 2023-06-05 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0007_alter_fatacids_monosatured_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="Category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="main.categories",
                verbose_name="Категория продукта",
            ),
        ),
    ]
