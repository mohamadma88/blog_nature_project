# Generated by Django 4.2.6 on 2023-11-03 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail_post_app', '0007_detail_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]
