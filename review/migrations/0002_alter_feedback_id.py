# Generated by Django 3.2.13 on 2023-06-13 20:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='id',
            field=models.UUIDField(default=uuid.UUID('bca79d26-259e-4e7c-b9a2-fd5c60db9604'), primary_key=True, serialize=False),
        ),
    ]
