class Category:
     
    def __init__(self,c):
        self.category=c
        self.ledger=[]
        
    def deposit(self,amount,description=""):
        self.ledger.append({"amount": amount, "description": description})

    def get_balance(self):
        total=0
        for transaction in self.ledger:
            total+=transaction["amount"]
        return total
        
    def check_funds(self,amount):
        if amount>self.get_balance():
            return False
        else:
            return True
    
    def withdraw(self,amount,description=""):
        if self.check_funds(amount)==False:
            return False
        else:
            self.ledger.append({"amount": -1*amount, "description": description})
            return True
    
    
    
    def transfer(self, amount, budget_category):
        if self.check_funds(amount)==True:

            self.ledger.append({'amount': -(amount),
      'description': f'Transfer to {budget_category.category}'})
            budget_category.deposit(amount, description = f'Transfer from {self.category}')
            return True 
        else:
            return False
    def __str__(self):
        length=len(self.category)
        rem_len=30-length
        title=""
        for _ in range(int(rem_len/2)):
            title+="*"
        title+=str(self.category)
        if rem_len%2==0:
            for _ in range(int(rem_len/2)):
                title+="*"
        else:
            for _ in range(int(rem_len/2)+1):
                title+="*"
        for transaction in self.ledger:
            description=transaction["description"]
            title+="\n"
            description=description[:23]
            l1=len(description)
            title += description
            amount=float(transaction["amount"])
            amount='%.2f'%amount
            l2=len(amount)
            lspaces=30-l1-l2
            title+=" "*lspaces
            title+=amount

        title+="\n"
        title+="Total: "+ '%.2f'%self.get_balance()
        return title
    
food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
print(food)    

def create_spend_chart(categories):
  spent_dict = {}
  for i in categories:
    s = 0 
    for j in i.ledger:
      if j['amount'] < 0 :
        s+= abs(j['amount'])
    spent_dict[i.category] = round(s,2)
  total = sum(spent_dict.values())
  percent_dict = {}
  for k in spent_dict.keys():
    percent_dict[k] = int(round(spent_dict[k]/total,2)*100)
  output = 'Percentage spent by category\n'
  for i in range(100,-10,-10):
    output += f'{i}'.rjust(3) + '| '
    for percent in percent_dict.values():
      if percent >= i:
        output+= 'o  '
      else:
        output+= '   '
    output += '\n' 
  output += ' '*4+'-'*(len(percent_dict.values())*3+1)
  output += '\n     '
  dict_key_list = list(percent_dict.keys())
  max_len_category = max([len(i) for i in dict_key_list])
  
  for i in range(max_len_category):
    
    for name in dict_key_list:
      if len(name)>i:
        output+= name[i] +'  '
      else:
        output+= '   '
    if i < max_len_category-1:
      output+='\n     '
    
  return output