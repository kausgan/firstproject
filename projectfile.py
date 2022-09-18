import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="zeezee22**++",
    database="online_booking_db"
 )  


mycursor=mydb.cursor()
#************************************
def enter_data(Your_place,Travel_day,Timing):

    sql="insert into ticket_booking (Your_place,Travel_day,Timing) values (%s,%s,%s)"

    val=(Your_place,Travel_day,Timing)

    mycursor.execute(sql,val)

    mydb.commit()
    print("data inserted")

user=int(input("enter your number:"))

if user==1:
    Your_place=input("enter your place:").lower().strip()

    Travel_day=input("enter your day: ").lower().strip()

    Timing=input("enter the timing:").lower().strip()


    enter_data(Your_place,Travel_day,Timing)







   







