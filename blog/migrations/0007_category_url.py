# Generated by Django 4.2.2 on 2024-02-28 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_category_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='url',
            field=models.CharField(max_length=100, null=True),
        ),
    ]