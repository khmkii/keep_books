from django.db import models
from django.utils import timezone

from accounts.choices import ACCOUNT_TYPE, ACCOUNT_SUBTYPE, ACTIONS, ASSET_TYPE, PERIOD_CHOICES


class BaseAccountModel(models.Model):
    creation_timestamp = models.DateTimeField(editable=False)
    modified_timestamp = models.DateTimeField()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        On save update modified timestamp, and set creation timestamp if row does not exist
        """

        if not self.id:
            self.creation_timestamp = timezone.now()
        self.modified = timezone.now()

        return super(BaseAccountModel, self).save(*args, **kwargs)


class AssetType(BaseAccountModel):
    asset_type = models.IntegerField(choices=ASSET_TYPE)


class Account(BaseAccountModel):
    account_code = models.IntegerField()
    account_name = models.CharField(max_length=100)
    account_type = models.IntegerField(choices=ACCOUNT_TYPE)
    account_subtype = models.IntegerField(choices=ACCOUNT_SUBTYPE)
    asset_type = models.ForeignKey(to=AssetType, on_delete=models.PROTECT, default=0)


class Journal(BaseAccountModel):
    transaction_date = models.DateField(default=timezone.now)
    transaction_amount = models.DecimalField(decimal_places=2, max_digits=12)
    action = models.IntegerField(choices=ACTIONS)
    account = models.ForeignKey(to=Account, on_delete=models.PROTECT)
    description = models.CharField(max_length=150, default='')
    transaction_reference = models.CharField(max_length=150, default='')
    uuid = models.CharField(default='', max_length=36)


class Posting(BaseAccountModel):
    account_id = models.ForeignKey(to=Account, on_delete=models.PROTECT)
    batch_reference = models.CharField(default='', max_length=36)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    accounting_period = models.IntegerField(choices=PERIOD_CHOICES)
    asset_type = models.ForeignKey(to=AssetType, on_delete=models.PROTECT, default=0)

# business segment? optional, usefull for later