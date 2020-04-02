# Generated by Django 2.2.6 on 2020-04-01 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gymnasium', '0004_notification'),
        ('users', '0002_studentprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medical_history', models.TextField(max_length=1000)),
                ('age', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('allergies', models.TextField(max_length=500)),
                ('address', models.TextField(max_length=500)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
                ('equipment_interest', models.ManyToManyField(related_name='equipment_interest', to='gymnasium.Equipmenttype')),
                ('gym_package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribed_package', to='gymnasium.Package')),
            ],
        ),
        migrations.DeleteModel(
            name='StudentProfile',
        ),
    ]