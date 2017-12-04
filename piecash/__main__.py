from PiecashUtil import PiecashUtil

if __name__ == '__main__':
    piecashUtil = PiecashUtil()
    piecashUtil.expenseTransaction(
        assetAccountFullName='Assets:Current Assets:Cash in Wallet', 
        expenseAccountFullName='Expenses:Supplies', 
        description='test',
        value=16)
    
    