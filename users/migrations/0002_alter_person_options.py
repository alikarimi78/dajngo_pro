# Generated by Django 5.1.1 on 2024-09-04 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['first_name']},
        ),
    ]
