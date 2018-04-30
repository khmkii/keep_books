from django.contrib import admin

from .models import Account, AssetType, Journal, Posting


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass


@admin.register(AssetType)
class AssetTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    pass


@admin.register(Posting)
class PostingAdmin(admin.ModelAdmin):
    pass
