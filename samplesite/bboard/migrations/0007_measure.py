# Generated by Django 4.1.7 on 2023-03-26 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0006_alter_bb_kind'),
    ]

    operations = [
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measurements', models.FloatField(choices=[(1.0, 'Метры'), (0.3048, 'Футы'), (0.9144, 'Ярды')])),
            ],
        ),
    ]