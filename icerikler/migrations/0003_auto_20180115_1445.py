# Generated by Django 2.0.1 on 2018-01-15 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icerikler', '0002_auto_20180115_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kategoriler',
            name='seo_title',
            field=models.SlugField(blank=True, editable=False, max_length=255, unique=True, verbose_name='Kategori Kısa İsmi'),
        ),
    ]