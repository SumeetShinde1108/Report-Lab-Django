# Generated by Django 4.2.16 on 2025-01-23 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Route",
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
                ("locations", models.CharField(max_length=32)),
                ("sequence", models.PositiveIntegerField()),
            ],
            options={
                "verbose_name": "01 Routes",
            },
        ),
        migrations.CreateModel(
            name="vehicle",
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
                ("vehicle_no", models.CharField(max_length=16)),
                ("average_speed", models.FloatField()),
                (
                    "capacity",
                    models.FloatField(help_text="Represents capacity of vehicle"),
                ),
                ("carrying_weight", models.FloatField()),
                ("remaining_weight", models.FloatField()),
                ("Total_Distance", models.FloatField()),
                (
                    "route",
                    models.ManyToManyField(
                        related_name="VehicleRoute", to="sample_app.route"
                    ),
                ),
            ],
            options={
                "verbose_name": "Vehicle",
                "verbose_name_plural": "02 Vehicles",
            },
        ),
    ]
