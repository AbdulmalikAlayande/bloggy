# Generated by Django 5.0.4 on 2024-04-20 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auths", "0002_user_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=30, verbose_name="Password"),
        ),
    ]