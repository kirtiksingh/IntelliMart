# Generated by Django 3.2.3 on 2021-05-24 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0020_auto_20210523_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.CharField(default='kg', max_length=20),
        ),
    ]
