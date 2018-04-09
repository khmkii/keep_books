from django.db import models
from django.utils import timezone


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
    pass


class Account(BaseAccountModel):
    code = models.IntegerField()
    name = models.CharField(max_length=100)
    type = models.IntegerField()


class Journal(BaseAccountModel):
    pass


class Posting(BaseAccountModel):
    account_id = models.ForeignKey(to=Account, on_delete=models.PROTECT)
    # one-to-one or many-to-one ?journal_id = models.ForeignKey(to=Journal, related_name=)
    asset_type = models.ForeignKey(to=AssetType, on_delete=models.PROTECT)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
