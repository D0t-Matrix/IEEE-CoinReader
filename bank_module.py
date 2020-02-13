import locale

class Bank():

    def __init__(self) -> None:
        '''
        Initializer. 
        Sets the balance and total money counters to zero
        '''
        self.bal = 0
        self.total_balance = 0

    def deposit(self, amount) -> bool:
        '''
        Adds deposit amount to the balance
        '''
        self.bal += amount
        self.total_balance += amount
        return True

    def withdraw(self, amount) -> bool:
        '''
        Removes amount from balance if funds are available.
        Returns False if unable to withrdraw funds, True otherwise.
        '''
        if (self.bal - amount) >= 0.0:
            self.bal -= amount
            return True
        else:
            return False

    def new_transaction(self) -> bool:
        '''
        resets balance of this transaction so that a new user can start
        '''
        self.bal = 0
        if self.bal != 0:
            return False
        else:
            return True

    def get_total(self) -> float:
        '''
        Gets the total amount of money added to machine
        '''
        return self.total_balance

    def get_balance(self) -> str:
        '''
        Gets the balance of this transaction
        '''
        locale.setlocale( locale.LC_ALL, 'English_United States.1252' )
        return locale.currency( bal, grouping = True )