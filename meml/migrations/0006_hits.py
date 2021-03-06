# Generated by Django 4.0.3 on 2022-03-22 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meml', '0005_rename_drug_interaction_druginteraction_drug_reaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hits',
            fields=[
                ('hit_id', models.AutoField(primary_key=True, serialize=False)),
                ('ip_address', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='meml.drug')),
            ],
            options={
                'db_table': 'hits',
                'managed': True,
            },
        ),
    ]
