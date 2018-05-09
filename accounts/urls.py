from django.urls import path
from accounts.views import AccountsHomeView, AccountsListView, JournalEntryView

app_name = 'accounts'

urlpatterns = [
    path(r'', AccountsHomeView.as_view(), name='home'),
    path(r'journal', JournalEntryView.as_view(), name='journal_entry'),
    path(r'accounts-list', AccountsListView.as_view(), name='accounts_list'),
]