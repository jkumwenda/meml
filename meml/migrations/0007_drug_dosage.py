# Generated by Django 4.0.3 on 2022-03-22 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meml', '0006_hits'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='dosage',
            field=models.TextField(blank=True, null=True),
        ),
    ]
