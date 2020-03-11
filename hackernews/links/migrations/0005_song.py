# Generated by Django 3.0.2 on 2020-03-09 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0004_album'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
