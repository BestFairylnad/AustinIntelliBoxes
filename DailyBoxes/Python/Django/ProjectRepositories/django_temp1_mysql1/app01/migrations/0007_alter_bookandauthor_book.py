# Generated by Django 3.2.6 on 2021-08-21 12:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_alter_bookandauthor_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookandauthor',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.book'),
        ),
    ]
