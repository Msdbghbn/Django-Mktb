# Generated by Django 3.2.13 on 2022-07-11 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tag',
            new_name='tags',
        ),
    ]
