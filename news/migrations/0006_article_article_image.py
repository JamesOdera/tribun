# Generated by Django 4.1.7 on 2023-03-23 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_remove_article_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(blank=True, null=True, upload_to='articles/'),
        ),
    ]
