# Generated by Django 3.1 on 2020-08-18 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0004_homes_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homes',
            name='address',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
