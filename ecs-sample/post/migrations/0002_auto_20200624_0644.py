# Generated by Django 2.2.3 on 2020-06-24 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateField(auto_now_add=True, db_index=True),
        ),
    ]
