from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from accounts.forms import BaseJournalFormSet, JournalForm


class JournalEntryView(LoginRequiredMixin, generic.CreateView):
    form_class = JournalForm
    template_name = ''

