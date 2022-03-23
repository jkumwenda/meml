# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DrugClass(models.Model):
    drug_class_id = models.AutoField(primary_key=True)
    drug_class = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'drug_class'

    def __str__(self):
        return self.drug_class


class Food(models.Model):
    food_id = models.AutoField(primary_key=True)
    food = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'food'

    def __str__(self):
        return self.food


class Drug(models.Model):
    drug_id = models.AutoField(primary_key=True)
    drug_class = models.ForeignKey('DrugClass', models.DO_NOTHING)
    drug_name = models.CharField(max_length=100)
    dosage = models.TextField(blank=True, null=True)
    manufacturer = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'drug'

    def __str__(self):
        return self.drug_name


class DrugReaction(models.Model):
    drug_reaction_id = models.AutoField(primary_key=True)
    drug = models.ForeignKey('Drug', models.DO_NOTHING)
    drug_reaction = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'drug_reaction'


class DrugInteraction(models.Model):
    drug_interaction_id = models.AutoField(primary_key=True)
    drug = models.ForeignKey('Drug', models.DO_NOTHING)
    drug_two = models.ForeignKey(
        'Drug', on_delete=models.CASCADE, related_name='drug_two')
    drug_reaction = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'drug_interaction'


class DrugFoodReaction(models.Model):
    drug_food_reaction_id = models.AutoField(primary_key=True)
    drug = models.ForeignKey('Drug', models.DO_NOTHING)
    food = models.ForeignKey('Food', models.DO_NOTHING)
    drug_food_reaction = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'drug_food_reaction'


class DrugContraindication(models.Model):
    drug_contraindication_id = models.AutoField(primary_key=True)
    drug = models.ForeignKey('Drug', models.DO_NOTHING)
    drug_contraindication = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'drug_contraindication'


class Hits(models.Model):
    hit_id = models.AutoField(primary_key=True)
    drug = models.ForeignKey('Drug', models.DO_NOTHING)
    ip_address = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'hits'
