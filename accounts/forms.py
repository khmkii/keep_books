from django.forms import ModelForm, formsets
from accounts.models import Journal


class JournalForm(ModelForm):

    class Meta:
        model = Journal
        fields = [
            'transaction_date',
            'transaction_reference',
            'description'
            'transaction_amount',
            'action',
        ]


class BaseJournalFormSet(formsets.BaseFormSet):

    def clean(self):
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