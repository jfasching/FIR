# Generated by Django 3.1.6 on 2021-02-09 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fir_alerting', '0002_add_helptext_to_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorytemplate',
            name='body',
            field=models.TextField(help_text='This is a Markdown field. You can use django templating language.'),
        ),
    ]
