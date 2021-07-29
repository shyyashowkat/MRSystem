# Generated by Django 3.2.4 on 2021-07-23 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(choices=[('action', 'action'), ('adventure', 'adventure'), ('animation', 'animation'), ('biography', 'biography'), ('comedy', 'comedy'), ('crime', 'crime'), ('drama', 'drama'), ('family', 'family'), ('fantasy', 'fantasy'), ('horror', 'horror'), ('mystery', 'mystery'), ('romance', 'romance'), ('thriller', 'thriller'), ('war', 'war')], max_length=16)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.movie')),
            ],
        ),
    ]