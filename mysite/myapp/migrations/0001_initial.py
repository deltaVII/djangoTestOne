# Generated by Django 4.2.1 on 2023-05-14 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('companyName', models.CharField(max_length=50, verbose_name='Имя компании')),
                ('companyNumber', models.IntegerField(unique=True, verbose_name='Номер компании')),
                ('companyPost', models.TextField(verbose_name='Описание компании')),
            ],
        ),
    ]
