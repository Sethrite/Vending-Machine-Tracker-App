# Generated by Django 5.1.2 on 2024-10-27 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0005_remove_snackspot_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snackspot',
            name='amount',
            field=models.IntegerField(default=8, null=True),
        ),
    ]
