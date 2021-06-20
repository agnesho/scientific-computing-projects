class Category:

  def __init__(self, category_name):
    self.name = category_name
    self.ledger = list()

  def deposit(self, amount, desc=None):
    if desc == None:
      desc = ""
    self.ledger.append({"amount": amount, "description": desc})
  
  def withdraw(self, amount, desc=""):
    if self.check_funds(amount): # if True
      self.ledger.append({"amount": -amount, "description": desc})
      return True
    else:
      return False

  def get_balance(self):
    self.balance = 0
    for entry in self.ledger:
      try:
        for v in entry.values():
          self.balance += v
      except:
        continue
    return self.balance

  def transfer(self, amount, category_name2):
    if self.check_funds(amount): # if True
      self.withdraw(amount, 'Transfer to ' + category_name2.name)
      category_name2.deposit(amount, 'Transfer from ' + self.name)
      return True
    else:
      return False

  def check_funds(self, amount):
    balance = self.get_balance()
    if amount > balance:
      return False
    else:
      return True

  def __str__(self):
    # Category name's length is even
    if len(self.name) % 2 == 0:
      output = ((30-len(self.name))//2)*'*' + self.name + ((30-len(self.name))//2)*'*' + '\n'
    # Odd
    else:
      output = ((30-len(self.name))//2 + 1)*'*' + self.name + ((30-len(self.name))//2)*'*' + '\n'

    for entry in self.ledger:
      item = entry["description"][:23]
      price = entry["amount"]
      output += '{:<23}{:>7.2f}\n'.format(item, price)

    output += 'Total: ' + '{:.2f}'.format(self.get_balance())

    return output


##### Bar Chart #####
def create_spend_chart(categories):
  total_spending = 0
  max_length = 0
  cat_list = list()
  per_list = list()

  # Find categories and their respective withdrawals
  for i in categories:
    for cat in i.ledger:
      if cat['amount'] < 0:
        spending = -cat['amount']
        total_spending += (-cat['amount'])

  # What is the length of the longest category name?
    if len(i.name) > max_length:
      max_length = len(i.name)
    
    cat_list.append([i.name, spending])

  for i in cat_list:
    percentage = (i[1]/total_spending)*100
    per_list.append({i[0]: percentage})
  
  # Output
  title = "Percentage spent by category\n"
  row = ''
  name = '     '
  no_of_categories = len(cat_list)
  
  for i in range(100,-10,-10):
    row += '{:3}{} '.format(i, '|')
    for j in per_list:
      for cat, percentage in j.items():
        if percentage >= i:
          row += 'o  '
        else:
          row += '   '
    row += '\n'
  
  count = 0
  for i in range(max_length):
    for j in cat_list:
      if len(j[0])-1 < count:
        name += '   '
      else:
        name += j[0][i] + '  '
    # No newline after last character
    if i == max_length-1:
      continue
    else:
      name += '\n     '
    count += 1
    
  dash = '    ' + '-' * (no_of_categories*3 + 1) + '\n'
  
  output = title + row + dash + name 

  return output