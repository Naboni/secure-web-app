# Generated by Django 4.1.7 on 2023-06-18 00:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0007_alter_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.UUIDField(
                auto_created=True,
                default=uuid.UUID("3b1a0f50-6a8e-4c60-93d5-1d377c7b5ba4"),
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
