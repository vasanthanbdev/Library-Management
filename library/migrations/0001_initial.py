# Generated by Django 5.0 on 2023-12-12 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_no', models.IntegerField()),
                ('title', models.TextField()),
                ('author', models.TextField()),
                ('status', models.CharField(default='AVAILABLE', max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]
