# Generated by Django 4.1.3 on 2022-11-24 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment4app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='one', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
