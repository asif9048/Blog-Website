# Generated by Django 4.2.4 on 2023-08-23 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog2', '0012_blogpost2_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost2',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
