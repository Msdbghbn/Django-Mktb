# Generated by Django 3.2.13 on 2022-07-11 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_commnet_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commnet',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
        ),
    ]
