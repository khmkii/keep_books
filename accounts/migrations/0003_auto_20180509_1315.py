# Generated by Django 2.0.4 on 2018-05-09 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180509_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='posted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='journal',
            name='uuid',
            field=models.CharField(default='', max_length=16),
        ),
        migrations.AddField(
            model_name='posting',
            name='asset_type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='accounts.AssetType'),
        ),
    ]