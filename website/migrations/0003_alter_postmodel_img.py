# Generated by Django 5.1.1 on 2024-12-11 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_rename_posts_postmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
