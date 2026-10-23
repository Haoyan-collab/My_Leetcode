class Bank:

    def __init__(self, balance: list[int]):
        self.hash_bank = {}
        for i,val in enumerate(balance):
            self.hash_bank[i+1] = val
    # account-> balance
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 not in self.hash_bank or account2 not in self.hash_bank:
            return False
        if self.hash_bank[account1] >= money:
            self.hash_bank[account1] -= money
            self.hash_bank[account2] += money
            return True
        return False
    # account-> balance
    def deposit(self, account: int, money: int) -> bool:
        if account not in self.hash_bank:
            return False
        self.hash_bank[account] += money
        return True
    
    def withdraw(self, account: int, money: int) -> bool:
        if account not in self.hash_bank:
            return False
        if self.hash_bank[account] >= money:
            self.hash_bank[account] -= money
            return True
        
        return False

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)