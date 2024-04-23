# Generated by Django 4.2 on 2024-02-24 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='postlabel',
            field=models.CharField(blank=True, choices=[('POPULAR', 'popular'), ('TRENDING', 'trending')], max_length=100, null=True),
        ),
    ]