# Generated by Django 4.0.4 on 2022-04-30 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_data_scrapyitem_text_scrapyitem_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scrapyitem',
            old_name='text',
            new_name='data',
        ),
        migrations.RemoveField(
            model_name='scrapyitem',
            name='author',
        ),
    ]