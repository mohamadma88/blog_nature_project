# Generated by Django 4.2.6 on 2023-10-30 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detail_post_app', '0004_remove_detail_create_detail_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='created',
        ),
    ]
