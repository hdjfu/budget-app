class Category:

  def __str__(self):
    rt = self.name.center(30, '*') + '\n'
    valor = 0
    for x in self.ledger:
      valor += x.get('amount')
      rt += x.get('description')[0:23].ljust(23, ' ') + format(
        x.get('amount'), '.2f').rjust(7, ' ')
      rt += '\n'
    rt += 'Total: ' + str(valor)
    return rt

  def __init__(self, category):
    self.ledger = []
    self.name = category
    self.deposito = 0
    self.allSpent = 0

  def check_funds(self, amount):
    return self.get_balance() >= amount

  def deposit(self, amount, description=''):
    obj = {"amount": amount, "description": description}
    self.ledger.append(obj)
    self.deposito += amount

  def withdraw(self, amount, description=''):
    obj = {"amount": -amount, "description": description}
    if self.check_funds(amount):
      self.ledger.append(obj)
      self.allSpent += amount
      return True
    else:
      return False

  def get_balance(self):
    founds = 0
    for x in self.ledger:
      founds += x.get("amount")
    return founds

  def transfer(self, amount, objeto):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + objeto.name)
      objeto.deposit(amount, "Transfer from " + self.name)
      return True
    return False


def create_spend_chart(categories):

  gastos = []
  for x in categories:
    gastos.append(x.allSpent)
  total = sum(gastos)
  percent = [
    100 * gastos[0] / total, 100 * gastos[1] / total, 100 * gastos[2] / total
  ]
  final = 'Percentage spent by category\n'
  numero = 100

  for x in range(11):
    final += str(numero).rjust(3, ' ') + '| '
    if percent[0] >= numero:
      final += 'o'
    else:
      final += ' '
    final += '  '
    if percent[1] >= numero:
      final += 'o'
    else:
      final += ' '
    final += '  '
    if percent[2] >= numero:
      final += 'o'
    else:
      final += ' '
    final += '  \n'

    numero -= 10
  final += '    ----------\n'

  names = [categories[0].name, categories[1].name, categories[2].name]
  maxNames = len(max(names, key=len))
  names[0] = names[0].ljust(maxNames, ' ')
  names[1] = names[1].ljust(maxNames, ' ')
  names[2] = names[2].ljust(maxNames, ' ')

  for x in range(maxNames):
    final += '     '+ names[0][x]+ '  ' + names[1][x]+ '  ' + names[2][x]+'  \n'
  final = final[:-1]
  return final
