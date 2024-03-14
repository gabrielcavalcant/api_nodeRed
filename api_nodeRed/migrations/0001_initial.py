# Generated by Django 5.0.3 on 2024-03-14 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor', models.BooleanField(default=False)),
                ('botao', models.BooleanField(default=False)),
                ('liga_robo', models.BooleanField(default=False)),
                ('reset_contador', models.BooleanField(default=False)),
                ('valor_contagem', models.IntegerField(default=0)),
            ],
        ),
    ]
