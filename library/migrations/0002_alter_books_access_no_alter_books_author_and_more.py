# Generated by Django 5.0 on 2023-12-12 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='access_no',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='books',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
