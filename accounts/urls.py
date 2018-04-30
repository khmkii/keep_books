from django.urls import path
from accounts.views import AccountsHomeView, JournalEntryView

app_name = 'accounts'

urlpatterns = [
    path(r'', AccountsHomeView.as_view()),
    path(r'journal', JournalEntryView.as_view())
]