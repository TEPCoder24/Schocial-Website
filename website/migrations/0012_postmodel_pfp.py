# Generated by Django 5.1.1 on 2024-12-15 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_alter_profilemodel_pfp'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='pfp',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
