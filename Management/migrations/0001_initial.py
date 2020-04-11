# Generated by Django 2.2.7 on 2020-04-09 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tournment',
            fields=[
                ('id', models.CharField(max_length=16, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.CharField(max_length=16, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=264)),
                ('owner', models.CharField(max_length=264)),
                ('tourn_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Management.Tournment')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.CharField(max_length=16, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=264)),
                ('skill', models.CharField(max_length=264)),
                ('runs', models.IntegerField(max_length=264)),
                ('wickets', models.IntegerField(max_length=264)),
                ('team_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Management.Teams')),
                ('tourn_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Management.Tournment')),
            ],
        ),
    ]
