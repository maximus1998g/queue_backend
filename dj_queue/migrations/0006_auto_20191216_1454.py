# Generated by Django 2.2.7 on 2019-12-16 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_queue', '0005_auto_20191216_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='decision',
            field=models.CharField(choices=[('ACCEPT', 'ACCEPT'), ('DECLINE', 'DECLINE')], default='DECLINE', max_length=10),
        ),
    ]