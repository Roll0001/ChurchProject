from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('TozymChurch_APP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='church_schedule',
            name='title_pl',
            field=models.CharField(blank=True, max_length=255, verbose_name='Назва польською'),
        ),
        migrations.AddField(
            model_name='church_schedule',
            name='title_ru',
            field=models.CharField(blank=True, max_length=255, verbose_name='Назва російською'),
        ),
        migrations.AddField(
            model_name='church_schedule',
            name='title_de',
            field=models.CharField(blank=True, max_length=255, verbose_name='Назва німецькою'),
        ),
        migrations.AddField(
            model_name='church_schedule',
            name='title_en',
            field=models.CharField(blank=True, max_length=255, verbose_name='Назва англійською'),
        ),
        migrations.AddField(
            model_name='church_schedule',
            name='description_pl',
            field=models.TextField(blank=True, verbose_name='Опис польською'),
        ),
        migrations.AddField(
            model_name='church_schedule',
            name='description_ru',
            field=models.TextField(blank=True, verbose_name='Опис російською'),
        ),
        migrations.AddField(
            model_name='church_schedule',
            name='description_de',
            field=models.TextField(blank=True, verbose_name='Опис німецькою'),
        ),
        migrations.AddField(
            model_name='church_schedule',
            name='description_en',
            field=models.TextField(blank=True, verbose_name='Опис англійською'),
        ),
    ]