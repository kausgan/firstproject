import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="zeezee22**++",
    database="hotel_management_db"
)



mycursor=mydb.cursor()
#********************************
print("*************WELCOME TO HOTEL MALALA***************")

def enter_food_items(your_name, food_name, dish_number,total_amount):

    sql="insert into food_items (your_name, food_name, dish_number,total_amount) values (%s,%s,%s,%s)"

    val=(your_name, food_name, dish_number,total_amount)

    mycursor.execute(sql,val)
    mydb.commit()

    print("FOOD ITEM IS READY")


user=int(input("enter your number:"))

if user==1:

   print("****todays offer 1 mutton briyani + 2 chicken gravy = 1 plane briyani free free free!!!")
   print("enjoy the dish")

   your_name=(input("enter your name:"))

   food_name=(input("enter your favorite dish:"))

   dish_number=(input("enter number of plates you want:"))

   total_amount=(input("your total amount is:"))

   enter_food_items(your_name, food_name, dish_number,total_amount)


if user==2:

    print("*******chilly chicken + mutton tandoori********")
    print("enjoy the dish")
    
    your_name=(input("enter your name:"))

    food_name=(input("enter your favorite dish:"))

    dish_number=(input("enter number of plates you want:"))

    total_amount=(input("your total amount is:"))

    enter_food_items(your_name, food_name, dish_number,total_amount)
 
  

if user==3:

    print("##***** MEALS WITH VADDA KARII GURMA AVAILABLE *****")
    print("2 plate meals = 2 vadda free free...!!")
    
    your_name=(input("enter your name:"))

    food_name=(input("enter your favorite dish:"))

    dish_number=(input("enter number of plates you want:"))

    total_amount=(input("your total amount is:"))

    enter_food_items(your_name, food_name, dish_number,total_amount)


if user==4:

    print ("******ALL FRESH JUICES AVAILABLE HERE********")

    print("WATERMELON + LEMON = RS.40")

    print("ORANGE + SUPPORTA = RS.50....only/-")
    
    print("******DON'T MISS THIS OFFER*****")

    
    your_name=(input("enter your name:"))

    food_name=(input("enter your favorite dish:"))

    dish_number=(input("enter number of plates you want:"))

    total_amount=(input("your total amount is:"))

    enter_food_items(your_name, food_name, dish_number,total_amount)


if user==5:

    print("*****VARIETY ICE CREAMS ARE AVAILABLE HERE********")

    print("venilla + strawberry = one cup rs.40")

    print("##### BUTTER SKOCTH #####")
    
    your_name=(input("enter your name:"))

    food_name=(input("enter your favorite dish:"))

    dish_number=(input("enter number of plates you want:"))

    total_amount=(input("your total amount is:"))

    enter_food_items(your_name, food_name, dish_number,total_amount)


if user==6:

    print("********* 2 SAMOSA + 1 PUPS = Rs.45")

    print("***** ENJOY YOUR CRISPY DAY ***** ")

    print("****** fish fry 1 plate = finger fry 2 pieces FREE FREE,,,!!!")

    
    your_name=(input("enter your name:"))

    food_name=(input("enter your favorite dish:"))

    dish_number=(input("enter number of plates you want:"))

    total_amount=(input("your total amount is:"))

    enter_food_items(your_name, food_name, dish_number,total_amount)
