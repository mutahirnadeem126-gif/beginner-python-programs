# bank withdrwal system

balance = 80000
acc_name = "mutahir"
password = 1234

name = input("Enter your acount name:")
passs = int(input("Enter your passwprd:"))

if balance >0:
    
    if(acc_name == name and passs == password):
        print("Account sucessfuly login" )
    elif(acc_name != name or passs != password):
        print("Access denied")

        ammount = int(input("Enter your withdrwal amount"))
        if(ammount<=balance):
            print("Withdrwal Sucessful")
        else:
            print("Not suffcient Balance")

remain = balance - ammount
print("Your remaining balance is:",remain)