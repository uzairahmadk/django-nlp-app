# Generated by Django 4.1.4 on 2022-12-30 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("textprocessor", "0007_remove_project_p_id_project_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="created",
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
