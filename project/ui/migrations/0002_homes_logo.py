# Generated by Django 3.1 on 2020-08-18 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homes',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
