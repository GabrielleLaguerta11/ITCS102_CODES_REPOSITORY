#Conditional Statement
import getpass

username = "gabo"
password = "gabby08"

user = input("Enter username --> ")
p = getpass.getpass("Enter password --> ")

if user == username and p == password :
	print("ACCESS GRANTED")
else :
	print("ACCESS DENIED")