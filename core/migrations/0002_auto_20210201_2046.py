# Generated by Django 3.1.6 on 2021-02-01 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='away_matches', to='core.team')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='home_matches', to='core.team')),
            ],
        ),
        migrations.CreateModel(
            name='Stadium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.country')),
            ],
        ),
        migrations.CreateModel(
            name='MatchPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_substitute', models.BooleanField()),
                ('minutes_played', models.IntegerField(blank=True, null=True)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.player')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='stadium',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.stadium'),
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_own_goal', models.BooleanField(blank=True, null=True)),
                ('minute', models.IntegerField()),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.player')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.team')),
            ],
        ),
        migrations.CreateModel(
            name='Assist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minute', models.IntegerField()),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.player')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.team')),
            ],
        ),
    ]
