# Generated by Django 4.2.6 on 2023-11-02 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus_app', '0002_alter_contactus_email_alter_contactus_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
