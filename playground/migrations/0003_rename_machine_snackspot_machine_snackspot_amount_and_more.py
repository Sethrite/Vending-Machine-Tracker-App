# Generated by Django 5.1.2 on 2024-10-24 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0002_rename_machine_snackspot_machine_snackspot_snack'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snackspot',
            old_name='Machine',
            new_name='machine',
        ),
        migrations.AddField(
            model_name='snackspot',
            name='amount',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='snackspot',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='snackspot',
            name='position',
            field=models.TextField(null=True),
        ),
    ]
