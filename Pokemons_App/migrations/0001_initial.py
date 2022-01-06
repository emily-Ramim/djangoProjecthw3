# Generated by Django 3.2 on 2022-01-06 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemons',
            fields=[
                ('name', models.CharField(db_column='Name', max_length=50, primary_key=True, serialize=False)),
                ('type', models.CharField(db_column='Type', max_length=50)),
                ('generation', models.IntegerField(db_column='Generation')),
                ('legendary', models.BooleanField(db_column='Legendary')),
                ('hp', models.IntegerField(db_column='HP')),
                ('attack', models.IntegerField(db_column='Attack')),
                ('defense', models.IntegerField(db_column='Defense')),
            ],
            options={
                'db_table': 'Pokemons',
                'managed': False,
            },
        ),
    ]