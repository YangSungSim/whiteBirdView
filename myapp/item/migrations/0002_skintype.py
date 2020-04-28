# Generated by Django 2.2.6 on 2020-04-07 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkinType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dry', models.CharField(choices=[(3, '보통이다'), (1, '매우아니다/매우작다/매우적다'), (2, '아니다/작다/적다'), (4, '그렇다/크다/많다'), (5, '매우그렇다/매우크다/매우 많다')], max_length=20)),
                ('sensitive', models.CharField(choices=[(3, '보통이다'), (1, '매우아니다/매우작다/매우적다'), (2, '아니다/작다/적다'), (4, '그렇다/크다/많다'), (5, '매우그렇다/매우크다/매우 많다')], max_length=20)),
                ('oily', models.CharField(choices=[(3, '보통이다'), (1, '매우아니다/매우작다/매우적다'), (2, '아니다/작다/적다'), (4, '그렇다/크다/많다'), (5, '매우그렇다/매우크다/매우 많다')], max_length=20)),
            ],
        ),
    ]
