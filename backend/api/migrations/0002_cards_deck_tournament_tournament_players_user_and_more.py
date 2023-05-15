# Generated by Django 4.2.1 on 2023-05-14 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65)),
                ('desc', models.CharField(max_length=200)),
                ('api_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65)),
                ('desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('date', models.DateTimeField(verbose_name='date it happens')),
            ],
        ),
        migrations.CreateModel(
            name='Tournament_players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=200)),
                ('tel', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
        migrations.AddField(
            model_name='tournament_players',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
        migrations.AddField(
            model_name='tournament_players',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tournament'),
        ),
        migrations.AddField(
            model_name='deck',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
        migrations.AddField(
            model_name='cards',
            name='deck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.deck'),
        ),
    ]