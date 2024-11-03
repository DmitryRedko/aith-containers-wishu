# Generated by Django 4.2.16 on 2024-11-03 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
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
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Время создания записи"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Время обновления записи"
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("date", models.DateField()),
                ("description", models.TextField()),
                ("repeat", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
