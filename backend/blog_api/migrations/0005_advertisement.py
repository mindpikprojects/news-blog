# Generated by Django 5.0.2 on 2024-03-01 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_api', '0004_alter_blog_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('url', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='ads_image')),
            ],
        ),
    ]
