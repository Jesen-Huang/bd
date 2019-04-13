# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.postgres import fields as pg_fields


class Authorities(models.Model):
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    username = models.ForeignKey('Users', models.DO_NOTHING, db_column='username')
    authority = models.CharField(max_length=128)
    enabled = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'authorities'
        unique_together = (('username', 'authority'),)


class Baiduitem(models.Model):
    name = models.CharField(max_length=200)
    url = models.TextField()
    text = models.TextField(blank=True, null=True)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'baiduitem'


class ContextInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    jibing_context = models.CharField(max_length=255, blank=True, null=True)
    rawcontent_id = models.IntegerField(blank=True, null=True)
    youyin_json = pg_fields.JSONField()

    class Meta:
        managed = False
        db_table = 'context_info'


class FreqLimit(models.Model):
    created = models.DateTimeField()
    updated = models.DateTimeField()
    token = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    duration = models.BigIntegerField()
    start_time = models.DateTimeField()
    last_time = models.DateTimeField()
    last_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'freq_limit'
        unique_together = (('token', 'name', 'duration', 'start_time'),)


class Icd10Jibing(models.Model):
    id = models.IntegerField(primary_key=True)
    bm = models.CharField(max_length=64)
    xh = models.IntegerField()
    fm = models.CharField(max_length=1024, blank=True, null=True)
    mc = models.CharField(max_length=1024)
    zjm = models.CharField(max_length=64)
    sm = models.TextField(blank=True, null=True)
    xbxz = models.CharField(max_length=8, blank=True, null=True)
    lxxz = models.TextField(blank=True, null=True)
    lb = models.CharField(max_length=8)
    flid = models.IntegerField()
    xtbs = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'icd10_jibing'


class Icd10Level(models.Model):
    id = models.IntegerField(primary_key=True)
    sjid = models.IntegerField(blank=True, null=True)
    xh = models.IntegerField()
    mc = models.CharField(max_length=1024)
    zjm = models.CharField(max_length=64, blank=True, null=True)
    lb = models.CharField(max_length=8)
    bmfw = models.CharField(max_length=1024, blank=True, null=True)
    sfbr = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'icd10_level'


class Icd10Level2Secondlevel(models.Model):
    id = models.IntegerField(primary_key=True)
    second_sjid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'icd10_level2secondlevel'


class IiItem(models.Model):
    id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    standname = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ii_item'


class IiRItemItem(models.Model):
    id = models.BigIntegerField(primary_key=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    from_item = models.ForeignKey(IiItem, models.DO_NOTHING, blank=True, null=True, related_name='to_items')
    to_item = models.ForeignKey(IiItem, models.DO_NOTHING, blank=True, null=True, related_name='from_items')

    class Meta:
        managed = True
        db_table = 'ii_r_item_item'
        unique_together = (('from_item', 'to_item'),)


class IiRJibingDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    detail_jsonb = pg_fields.JSONField()
    uuid = models.CharField(max_length=255, blank=True, null=True)
    jibing = models.OneToOneField(IiItem, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ii_r_jibing_detail'


class IiRJibingRule(models.Model):
    id = models.BigIntegerField(primary_key=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    items = pg_fields.ArrayField(models.IntegerField())
    jibing = models.ForeignKey(IiItem, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ii_r_jibing_rule'


class Jibing(models.Model):
    id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jibing'


class RJibingYouyin(models.Model):
    id = models.BigIntegerField(primary_key=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    context_info = models.ForeignKey(ContextInfo, models.DO_NOTHING, blank=True, null=True)
    jibing = models.ForeignKey(Jibing, models.DO_NOTHING, blank=True, null=True)
    youyin = models.ForeignKey('Youyin', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'r_jibing_youyin'


class TimeLimit(models.Model):
    created = models.DateTimeField()
    updated = models.DateTimeField()
    token = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    start_hour = models.IntegerField()
    end_hour = models.IntegerField()
    last_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'time_limit'
        unique_together = (('token', 'name', 'start_hour', 'end_hour'),)


class Users(models.Model):
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    username = models.CharField(primary_key=True, max_length=128)
    tenant = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    enabled = models.BooleanField()
    comments = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'users'


class Youyin(models.Model):
    id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'youyin'
