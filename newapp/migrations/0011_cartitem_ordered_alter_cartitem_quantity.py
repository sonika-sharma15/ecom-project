# Generated by Django 5.0.6 on 2024-08-21 15:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("newapp", "0010_cart"),
    ]

    operations = [
        migrations.AddField(
            model_name="cartitem",
            name="ordered",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="cartitem",
            name="quantity",
            field=models.PositiveIntegerField(default=1),
        ),
    ]