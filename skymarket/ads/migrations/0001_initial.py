# Generated by Django 4.1.2 on 2022-10-31 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='название товара')),
                ('price', models.PositiveIntegerField()),
                ('description', models.TextField(null=True, verbose_name='описание товара')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания объявления')),
                ('image', models.ImageField(null=True, upload_to='django_media/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ads', to='users.user')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000, verbose_name='текст отзыва')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания отзыва')),
                ('ad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ads.ad')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
