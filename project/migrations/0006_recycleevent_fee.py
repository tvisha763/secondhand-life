# Generated by Django 4.2.4 on 2023-10-15 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_recycleevent'),
    ]

    operations = [
        migrations.AddField(
            model_name='recycleevent',
            name='fee',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
