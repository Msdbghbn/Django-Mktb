# Generated by Django 3.2.13 on 2022-07-10 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_newsletter'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='email',
            field=models.EmailField(max_length=255, null=True),
        ),
    ]
