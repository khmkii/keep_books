from django.forms import BaseModelFormSet
from accounts.models import Journal


class BaseJournalFormSet(BaseModelFormSet):

    def clean(self):
        super().clean()
        if any(self.errors):
            return

        sum_debits = 0
        sum_credits = 0

        for form in self.forms:
            if form.cleaned_data:
                action = form.cleaned_data['action']
                amount = form.cleaned_data['transaction_amount']
                if action == 'debit':
                    sum_debits += amount
                else:
                    sum_credits += amount
