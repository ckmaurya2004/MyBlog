# Generated by Django 4.2.2 on 2024-02-26 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_category_desc_alter_post_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='url',
        ),
    ]
