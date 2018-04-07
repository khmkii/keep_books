from django.db import models
from django.utils import timezone


class BaseAccountModel(models.Model):
    creation_timestamp = models.DateTimeField(editable=False)
    modified_timestamp = models.DateTimeField()

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
    name = models.CharField()
    type = models.IntegerField()


class Journal(BaseAccountModel):
    pass


class Posting(BaseAccountModel):
    pass