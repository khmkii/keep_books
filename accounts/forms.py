from django.forms import BaseModelFormSet
from accounts.models import Journal


class BaseJournalFormSet(BaseModelFormSet):

    def clean(self):
        super().clean()
        if any(self.errors):
            return
