import datetime

PURCHASE = 0
EXPENSE = 1
ASSET = 2
REVENUE = 3
LIABILITY = 4
EQUITY = 5
CONTRA_ASSET = 6

ACCOUNT_TYPE = (
    (PURCHASE, 'Purchase'),
    (EXPENSE, 'Expense'),
    (ASSET, 'Asset'),
    (REVENUE, 'Revenue'),
    (LIABILITY, 'Liability'),
    (EQUITY, 'Equity'),
    (CONTRA_ASSET, 'Contra-Asset')
)

ACCOUNTS_RECEIVABLE = 0
ACCOUNTS_PAYABLE = 1

ACCOUNT_SUBTYPE = (
    (ACCOUNTS_RECEIVABLE, 'accounts receivable'),
    (ACCOUNTS_PAYABLE, 'accounts payable')
)

GBP = 0
USD = 1


ASSET_TYPE = (
    (GBP, '£'),
    (USD, '$')
)

PERIOD_CHOICES = [(e, y) for e, y in enumerate(range(2014, datetime.datetime.now().year + 1))]
