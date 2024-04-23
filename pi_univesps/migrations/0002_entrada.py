# Generated by Django 5.0.4 on 2024-04-23 17:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pi_univesps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('data_add', models.DateTimeField(auto_now_add=True)),
                ('topico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pi_univesps.campanha')),
            ],
            options={
                'verbose_name_plural': 'entradas',
            },
        ),
    ]