# Generated by Django 5.1.1 on 2024-12-14 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_profilemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='grade',
            field=models.SmallIntegerField(),
        ),
    ]
