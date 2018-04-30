# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-25 08:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_timestamp', models.DateTimeField(editable=False)),
                ('modified_timestamp', models.DateTimeField()),
                ('account_code', models.IntegerField()),
                ('account_name', models.CharField(max_length=100)),
                ('account_type', models.IntegerField(choices=[(0, 'Purchase'), (1, 'Expense'), (2, 'Asset'), (3, 'Revenue'), (4, 'Liability'), (5, 'Equity')])),
                ('account_subtype', models.IntegerField(choices=[(0, 'accounts receivable'), (1, 'accounts payable')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AssetType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_timestamp', models.DateTimeField(editable=False)),
                ('modified_timestamp', models.DateTimeField()),
                ('asset_type', models.IntegerField(choices=[(0, '£'), (1, '$')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_timestamp', models.DateTimeField(editable=False)),
                ('modified_timestamp', models.DateTimeField()),
                ('transaction_date', models.DateField(default=django.utils.timezone.now)),
                ('transaction_amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('action', models.IntegerField(choices=[(0, 'debit'), (1, 'credit')])),
                ('description', models.CharField(default='', max_length=150)),
                ('transaction_reference', models.CharField(default='', max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_timestamp', models.DateTimeField(editable=False)),
                ('modified_timestamp', models.DateTimeField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('accounting_period', models.IntegerField(choices=[(0, 2014), (1, 2015), (2, 2016), (3, 2017), (4, 2018)])),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.Account')),
                ('asset_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.AssetType')),
                ('journal_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.Journal')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]