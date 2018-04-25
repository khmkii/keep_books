from django.urls import path
from accounts.views import JournalEntryView

app_name = 'accounts'

urlpatterns = [
    path(r'journal', JournalEntryView.as_view())
]