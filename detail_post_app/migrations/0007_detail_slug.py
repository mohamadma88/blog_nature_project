# Generated by Django 4.2.6 on 2023-10-30 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail_post_app', '0006_detail_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
