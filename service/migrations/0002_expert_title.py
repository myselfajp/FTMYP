# Generated by Django 4.1.6 on 2023-02-15 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expert',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]