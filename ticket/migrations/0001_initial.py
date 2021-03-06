# Generated by Django 3.0.7 on 2021-08-13 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Metro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('mobile', models.CharField(blank=True, max_length=200, null=True)),
                ('startplace', models.CharField(blank=True, max_length=200, null=True)),
                ('endplace', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(choices=[('inprocess', 'In Process'), ('completed', 'Completed'), ('notstarted', 'Not Started')], default='notstarted', max_length=10)),
            ],
        ),
    ]
