# Generated by Django 5.0.2 on 2024-03-01 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_api', '0002_categories_image_alter_blog_postlabel'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
