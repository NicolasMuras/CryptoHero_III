# Generated by Django 3.1.6 on 2021-02-13 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'verbose_name': 'Album', 'verbose_name_plural': 'Albumes'},
        ),
        migrations.AlterModelOptions(
            name='artist',
            options={'verbose_name': 'Artista', 'verbose_name_plural': 'Artistas'},
        ),
        migrations.AddField(
            model_name='song',
            name='track_id',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='album',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='artistas/', verbose_name='Tapa'),
        ),
    ]
