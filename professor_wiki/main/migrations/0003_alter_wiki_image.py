# Generated by Django 5.2.2 on 2025-06-09 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_wiki_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wiki',
            name='image',
            field=models.ImageField(blank=True, height_field=100, null=True, upload_to='', width_field=75),
        ),
    ]
