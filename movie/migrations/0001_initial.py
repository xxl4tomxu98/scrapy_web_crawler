# Generated by Django 4.0.4 on 2022-04-30 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Título')),
                ('critics_consensus', models.TextField(blank=True, null=True, verbose_name='Consenso da crítica')),
                ('average_grade', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, verbose_name='Nota média')),
                ('poster', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Capa')),
                ('amount_reviews', models.PositiveIntegerField(blank=True, null=True, verbose_name='Quantidade de criticas')),
                ('approval_percentage', models.PositiveIntegerField(blank=True, null=True, verbose_name='Porcentagem de aprovação')),
            ],
        ),
    ]