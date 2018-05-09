from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError, transaction
from django.forms import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.generic import ListView, TemplateView, View
import uuid

from accounts.forms import BaseJournalFormSet
from accounts.models import Account, Journal


class AccountsHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/accounts_home.html'


class AccountsListView(LoginRequiredMixin, ListView):
    template_name = 'accounts/accounts_list.html'
    model = Account
    context_object_name = 'accounts'


class JournalEntryView(LoginRequiredMixin, View):
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
            extra=2
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

    def post(self, request, *args, **kwargs):

        unique_identifier = str(uuid.uuid4())

        journal_formset = self.JournalFormset(data=request.POST)

        if journal_formset.is_valid():

            new_entries = []

            for journal_entry in journal_formset:
                new_entries.append(journal_entry)

            try:
                with transaction.atomic():
                    Journal.objects.bulk_create(new_entries)
                    messages.success(request, message="Journal entries added")
            except IntegrityError:
                messages.error(request, "Error - please check journal entries balance")
                return redirect(reverse("accounts:journal_entry"))

