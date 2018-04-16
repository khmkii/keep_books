from django.contrib import admin

from .models import Account, AssetType, Journal, Posting


@admin.register(Account)
class SalesContractAdmin(admin.ModelAdmin):
    pass


@admin.register(AssetType)
class SalesContractAdmin(admin.ModelAdmin):
    pass


@admin.register(Journal)
class SalesContractAdmin(admin.ModelAdmin):
    pass


@admin.register(Posting)
class SalesContractAdmin(admin.ModelAdmin):
    pass
