# Generated by Django 4.2.6 on 2023-11-02 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus_app', '0004_alter_contactus_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
    ]