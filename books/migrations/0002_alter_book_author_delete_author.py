# Generated by Django 4.2.7 on 2023-11-23 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book", name="author", field=models.CharField(max_length=512),
        ),
        migrations.DeleteModel(name="Author",),
    ]