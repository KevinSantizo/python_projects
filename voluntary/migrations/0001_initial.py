# Generated by Django 2.2.3 on 2019-07-23 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('org_tel', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('act_name', models.CharField(max_length=255)),
                ('type', models.IntegerField(choices=[(1, 'Salud'), (2, 'Alimentación'), (3, 'Instrucción')])),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('requeriment', models.TextField()),
                ('description', models.TextField()),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voluntary.Organization')),
            ],
        ),
    ]
