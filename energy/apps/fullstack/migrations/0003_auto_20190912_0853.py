# Generated by Django 2.2.5 on 2019-09-12 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("fullstack", "0002_auto_20190912_0847")]

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
            ],
            options={
                "verbose_name": "employee",
                "verbose_name_plural": "employees",
                "ordering": ["name"],
            },
        ),
        migrations.AlterModelOptions(
            name="location",
            options={
                "ordering": ["name"],
                "verbose_name": "location",
                "verbose_name_plural": "locations",
            },
        ),
        migrations.AddField(
            model_name="event",
            name="employees",
            field=models.ManyToManyField(to="fullstack.Employee"),
        ),
    ]