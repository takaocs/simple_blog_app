# Generated by Django 3.0.4 on 2020-03-23 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='contents',
            field=models.TextField(blank=True, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(blank=True, max_length=100, verbose_name='タイトル'),
        ),
    ]
