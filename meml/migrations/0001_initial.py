# Generated by Django 4.0.3 on 2022-03-20 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('drug_id', models.AutoField(primary_key=True, serialize=False)),
                ('drug_name', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'drug',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DrugClass',
            fields=[
                ('drug_class_id', models.AutoField(primary_key=True, serialize=False)),
                ('drug_class', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'drug_class',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('food_id', models.AutoField(primary_key=True, serialize=False)),
                ('food', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'food',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DrugReaction',
            fields=[
                ('drug_reaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('drug_reaction', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('drug_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drug_one', to='meml.drug')),
                ('drug_two', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drug_two', to='meml.drug')),
            ],
            options={
                'db_table': 'drug_reaction',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DrugInteraction',
            fields=[
                ('drug_interaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('reaction', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='meml.drug')),
            ],
            options={
                'db_table': 'drug_interaction',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DrugFoodReaction',
            fields=[
                ('drug_food_reaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('drug_food_reaction', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='meml.drug')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='meml.food')),
            ],
            options={
                'db_table': 'drug_food_reaction',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DrugContraindication',
            fields=[
                ('drug_contraindication_id', models.AutoField(primary_key=True, serialize=False)),
                ('drug_contraindication', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='meml.drug')),
            ],
            options={
                'db_table': 'drug_contraindication',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='drug',
            name='drug_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='meml.drugclass'),
        ),
    ]