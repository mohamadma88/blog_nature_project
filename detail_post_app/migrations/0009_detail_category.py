# Generated by Django 4.2.6 on 2023-11-03 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('detail_post_app', '0008_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='detail_post_app.category'),
        ),
    ]