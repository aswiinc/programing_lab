
class bankaccount:
	def __init__(self,name,ac_type,balance=0):
		self.name=name
		self.ac_type=ac_type
		self.balance=balance
	

	def withdraw(self):
		amount=int(input("Enter the amount : "))
		if(amount>self.balance):
			print("Insufficent Balance : ")
		else:
			self.balance=self.balance-amount
	def deposit(self):
		amount=int(input("Enter the amount : "))
		self.balance=self.balance+amount
	def checkBalance(self):
		print(f"Account Balance= {self.balance}")


name=input("Enter the Name : ")
ac_type=input("Enter the Account Type : ")
obj=bankaccount(name,ac_type)
print("+-+-+-+-+-+-+-+-+")
print("1.Deposit \n 2. Withdrawal \n 3.Check Balance \n 4.Exit")
print("+-+-+-+-+-+-+-+-+")
while 1:
	choice=int(input("Enter your Choice : "))
	if(choice==1):
		obj.deposit()
	elif(choice==2):
		obj.withdraw()
	elif(choice==3):
		obj.checkBalance()
	elif(choice==4):
		exit()

		
	
		
		
		
		

	
