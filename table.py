import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="zeezee22**++",
    database="atm_machine_db"


)


mycursor=mydb.cursor()
#*******************************
print("************### WELCOME TO ATM MACHINE **********###")

def enter_data(name,account_number,deposit_amount,pin_number):

    sql="insert into login_machine (name,account_number,deposit_amount,pin_number) values (%s,%s,%s)"

    val=(name,account_number,deposit_amount,pin_number)

    mycursor.execute(sql,val)

    mydb.commit()

    print("LOGIN SUCCESS")


user=int(input("enter your number:"))

if user==1:
    print("welcome to withdraw your cash")

    name=input("enter your name:").lower().strip()

    account_number=int(input("enter your acc number:"))

   
    deposit_amount=int(input("enter your amount:"))

    pin_number=int(input("enter your pin:"))


    enter_data(name,account_number,deposit_amount,pin_number)


if user==2:

    print("welcome to deposit your cash")

    name=input("enter your name:").lower().strip()

    account_number=int(input("enter your acc number:"))

    deposit_amount=int(input("enter the amount:"))

    pin_number=int(input("enter your pin number:"))

    enter_data(name,account_number,deposit_amount,pin_number)

    
if user==3:

    print("BALANCE ENQUIRY")

    name=input("enter your name:").lower().strip()

    account_number=int(input("enter your pin number:"))

    deposit_amount=int(input("enter yes if want:"))

    pin_number=int(input("enter your acc number:"))

    enter_data(name,account_number,deposit_amount,pin_number)


if user==4:

    print("PIN GENERATION")

    name=input("enter the your name:")

    account_number=int(input("enter your acc number:"))

    deposit_amount=int(input("enter the deposit amount:"))

    pin_number=int(input("enter the pin number:"))

   

    enter_data(name,account_number,deposit_amount,pin_number)


if user==5:

    print("CHANGING THE PIN NUMBER")

    name=input("enter your name:")

    account_number=int(input("enter your account number:"))

    deposit_amount=int(input("enter your deeposit amount:"))

    pin_number=int(input("enter your pin number:"))

    enter_data(name,account_number,deposit_amount,pin_number)





        


