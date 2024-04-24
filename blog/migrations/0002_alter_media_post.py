# Generated by Django 5.0.4 on 2024-04-24 19:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="media",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="medias",
                to="blog.post",
                verbose_name="Post",
            ),
        ),
    ]
