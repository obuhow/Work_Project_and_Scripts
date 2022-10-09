# Generated by Django 4.1.1 on 2022-10-08 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublishedPosts',
            fields=[
                ('bot_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bot.bot')),
            ],
            options={
                'verbose_name': 'Опубликованные посты',
                'verbose_name_plural': 'Опубликованные посты',
            },
            bases=('bot.bot',),
        ),
        migrations.AlterField(
            model_name='bot',
            name='post',
            field=models.TextField(default='Этот пост еще не написан', verbose_name='Пост'),
        ),
        migrations.AlterField(
            model_name='bot',
            name='sending_datetime',
            field=models.CharField(default='2022-10-08 22:06:06', max_length=20, verbose_name='Дата отправки'),
        ),
        migrations.AlterField(
            model_name='bot',
            name='url',
            field=models.CharField(default='https://sweetspeak.ru/', max_length=256, verbose_name='URL статьи'),
        ),
    ]
