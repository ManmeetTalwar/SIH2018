# Generated by Django 2.0.3 on 2018-03-30 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0004_blockmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='scan',
            name='text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
