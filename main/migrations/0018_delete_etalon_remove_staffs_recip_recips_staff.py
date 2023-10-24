# Generated by Django 4.1.9 on 2023-06-24 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0017_chemicalsrecip_aminoacidcompositionrecip"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Etalon",
        ),
        migrations.RemoveField(
            model_name="staffs",
            name="recip",
        ),
        migrations.AddField(
            model_name="recips",
            name="staff",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="main.staffs"
            ),
            preserve_default=False,
        ),
    ]