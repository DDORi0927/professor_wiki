# Generated by Django 5.2.2 on 2025-06-09 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wiki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=15)),
                ('office', models.CharField(max_length=100)),
                ('college', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=150)),
                ('contents', models.TextField()),
            ],
        ),
    ]
