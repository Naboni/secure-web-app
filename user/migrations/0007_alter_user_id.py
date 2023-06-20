# Generated by Django 4.1.7 on 2023-06-18 00:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0006_alter_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.UUIDField(
                auto_created=True,
                default=uuid.UUID("9c9768e9-9413-4a9e-9de5-783231efaaea"),
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
