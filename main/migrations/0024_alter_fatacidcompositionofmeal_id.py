# Generated by Django 4.2.2 on 2023-07-17 17:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0023_alter_aminoacidcomposition_product_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fatacidcompositionofmeal",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
