'''
Created on Dec 3, 2017

@author: fangi
'''

from datetime import datetime
from piecash import open_book, Account, Transaction, Split, Commodity
from piecash.core.factories import create_currency_from_ISO
import piecash.core.account
from piecash.core.factories import single_transaction

class PiecashUtil(object):
    DB_CONN_STRING = 'mysql://gnucash:gnucash@localhost/gnucash'
    GNUCASH_CURRENCY = 'EUR'
    GNUCASH_ACCOUNT_TYPE_ASSETS = 'ASSET'
    GNUCASH_ACCOUNT_TYPE_EXPENSES = 'EXPENSE'

    def __init__(self):
        self.book = open_book(uri_conn=self.DB_CONN_STRING, readonly=False, do_backup=False)

    def expenseTransaction(self, assetAccountFullName, expenseAccountFullName, description, value):
        today = datetime.now()

        single_transaction(
            post_date=today,
            enter_date=today,
            description=description,
            value=value,
            from_account=self.book.accounts(fullname=assetAccountFullName),
            to_account=self.book.accounts(fullname=expenseAccountFullName))

        self.book.save()
