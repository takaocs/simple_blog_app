# Generated by Django 3.0.4 on 2020-03-22 00:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='タイトル')),
                ('contents', models.TextField(verbose_name='内容')),
                ('is_open', models.BooleanField(default=False, verbose_name='公開フラグ')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='削除フラグ')),
                ('record_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日時')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('open_time', models.DateTimeField(blank=True, null=True, verbose_name='公開日時')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': '投稿記事【Article】',
                'db_table': 'article',
            },
        ),
    ]