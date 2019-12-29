# Generated by Django 2.2.6 on 2019-12-29 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipmenttype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField(max_length=4)),
                ('timings', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Package',
                'verbose_name_plural': 'Packages',
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_of_purchase', models.DateField()),
                ('equipment_type', models.ForeignKey(on_delete=None, to='gymnasium.Equipmenttype')),
            ],
            options={
                'verbose_name': 'Equipment',
                'verbose_name_plural': 'Equipments',
            },
        ),
        migrations.CreateModel(
            name='AMC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('renewal_date', models.DateField()),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gymnasium.Equipment')),
            ],
            options={
                'verbose_name': 'AMC',
                'verbose_name_plural': 'AMC',
            },
        ),
    ]
