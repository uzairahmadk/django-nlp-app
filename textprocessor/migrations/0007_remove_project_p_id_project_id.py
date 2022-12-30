# Generated by Django 4.1.4 on 2022-12-30 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("textprocessor", "0006_remove_project_id_project_p_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="p_id",
        ),
        migrations.AddField(
            model_name="project",
            name="id",
            field=models.AutoField(
                auto_created=True,
                default=8,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
            preserve_default=False,
        ),
    ]
