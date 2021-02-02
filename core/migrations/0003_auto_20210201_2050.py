# Generated by Django 3.1.6 on 2021-02-01 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210201_2046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'countries'},
        ),
        migrations.AlterModelOptions(
            name='match',
            options={'verbose_name_plural': 'matches'},
        ),
        migrations.AddField(
            model_name='match',
            name='season',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='core.season'),
            preserve_default=False,
        ),
    ]
