# Generated by Django 3.2.13 on 2022-07-11 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_commnet_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Commnet',
        ),
    ]