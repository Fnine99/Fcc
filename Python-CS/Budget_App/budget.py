
class Category:
    

    def __init__(self, description) -> None:
        self.description = description
        self.balance = 0.0
        self.ledger = []

    def __repr__(self) -> str:
        ledger = ''
        header = self.description.center(30, '*') + '\n'
        for element in self.ledger:
            description_line = '{:<23}'.format(element['description'])
            amount_line = '{:7.2f}'.format(element['amount'])
            ledger += '{}{}\n'.format(description_line[:23], amount_line[:7])
        total = 'Total: {:.2f}'.format(self.balance)
             
        return header + ledger + total
        
    
    def deposit(self, amount, description='') -> None:
        self.balance += amount
        self.ledger.append({"amount": amount, "description": description})
    
    def check_funds(self, amount) -> bool:
        if self.balance >= amount:
          return True
        else:
          return False


    def withdraw(self, amount, description='') -> bool:
        if self.check_funds(amount):
            self.balance -= amount
            self.ledger.append({"amount": -1*amount, "description": description})
            return True
        else:
            return False


    def get_balance(self) -> int:
        return self.balance
        

    def transfer(self, amount, category=None) -> bool:
        if self.check_funds(amount):
            self.withdraw(amount, 'Transfer to {}'.format(category.description))
            category.deposit(amount, 'Transfer from {}'.format(self.description))
            return True
        else:
            return False
    

def create_spend_chart(categories):
    spend_amount = []

    for category in categories:
        spend = 0
        for element in category.ledger:
            if element['amount'] < 0 :
                spend = abs(element['amount'])
        spend_amount.append(round(spend, 2))
    
    total = round(sum(spend_amount), 2)
    spend_percentage = list(map(lambda amount: int((((amount/total)*10)//1)*10), spend_amount))

    headear_2 = 'Percentage spent by category\n'

    bar_chart = ''
    for element in reversed(range(0,101,10)):
        bar_chart += str(element).rjust(3)+'|'
        for percentage in spend_percentage:
            if percentage >= element:
                bar_chart += ' o '
            else:
                bar_chart += '   '
        bar_chart += ' \n'

    footer = '    ' + '-'*((3*len(categories))+1) +'\n'
    descriptions = list(map(lambda category: category.description, categories))
    max_length = max(map(lambda description: len(description), descriptions))
    descriptions = list(map(lambda description: description.ljust(max_length), descriptions))
    for i in zip(*descriptions):
        footer += '    ' + ''.join(map(lambda s: s.center(3), i))+' \n'

    return (headear_2 + bar_chart + footer).rstrip('\n')

