# Generated by Django 3.2.17 on 2023-02-07 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]