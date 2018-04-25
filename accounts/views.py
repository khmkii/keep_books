from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from accounts.forms import BaseJournalFormSet
from accounts.models import Journal


class JournalEntryView(View):
    JournalFormset = modelformset_factory(
            model=Journal,
            fields=(
               'transaction_date',
                'transaction_reference',
                'description',
                'transaction_amount',
                'action',
            ),
            formset=BaseJournalFormSet,
            max_num=25,
            extra=1
        )
    template_name = 'accounts/journal_entry.html'

    def get(self, request, *args, **kwargs):
        journal_formset = self.JournalFormset(queryset=Journal.objects.none())
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'journal_formset': journal_formset
            }
        )

    def post(self):
        pass

