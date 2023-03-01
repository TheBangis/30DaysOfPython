'''Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and 
it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. 
Incomes is a set of incomes and its description. The same goes for expenses.
'''
class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []
   
    def add_income(self, monie, descrpt):
        self.incomes.append((monie, descrpt))
    
    def add_expense(self, exp, descrpt):
        self.expenses.append((exp, descrpt))

    def total_income(self):
        total = 0
        for i in self.incomes:
            total+=i[0]
        return total
    
    def total_expense(self):
        total_exp = 0
        for expense in self.expenses:
            total_exp+=expense[0]
        return total_exp
    
    def account_balance(self):
        acc_bal = self.total_income() - self.total_expense()
        return acc_bal
    
    def account_info(self):
        print(F"fullname: {self.firstname} {self.lastname}")
        print(F"incomes: {self.incomes}")
        print(F"expenses: {self.expenses}")
        print(F"total incomes: {self.total_income()}")
        print(F"total expenses: {self.total_expense()}")
        print(F"account balance: {self.account_balance()}")

        

person = PersonAccount('babangida', 'sani')
person.add_income(200, 'allowance')
person.add_income(1000, "salary")
person.add_expense(50, 'biscuit')
person.add_expense(10, "pure water")
person.account_info()
