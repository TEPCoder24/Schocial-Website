# Generated by Django 5.1.1 on 2024-12-14 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_postmodel_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='post_images/'),
        ),
    ]
