# Generated by Django 4.1.7 on 2023-03-26 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0003_bb_kind_bb_types_of_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='kind',
            field=models.CharField(choices=[(None, 'Выберите тип публикуемого объявления'), ('b', 'Куплю'), ('s', 'Продам'), ('c', 'Обменяю'), ('r', 'Rent')], default='s', max_length=1),
        ),
    ]