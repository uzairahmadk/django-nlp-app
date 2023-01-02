# Generated by Django 4.1.4 on 2022-12-30 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("textprocessor", "0004_delete_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="department",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="textprocessor.department",
            ),
        ),
    ]