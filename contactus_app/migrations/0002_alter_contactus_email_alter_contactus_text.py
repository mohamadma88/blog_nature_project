# Generated by Django 4.2.6 on 2023-11-02 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
