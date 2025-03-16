#Air Ticket Booking System Project
print("\t\t\t\tWELCOME TO DOMESTIC AIRLINES")
import csv
import os
import random
import string

#INITIALIZING RECORDS/COLUMNS
try:
    with open("flightrecord.csv", "x") as fout:
        obj = csv.writer(fout)
        obj.writerow(["FLIGHT NUMBER", "SEAT", "FROM", "TO", "TIMINGS", "DATE", "PASSENGER'S NAME", "PASSENGER'S AGE", "PASSENGER'S MOBILE NUMBER"])
except FileExistsError:
    pass

#Add New Booking
def addrecord():
    print("\n\t\t\t\tADD A NEW RECORD")
    print("====================================================================================")
    fout=open("flightrecord.csv","a+")
    objct=csv.writer(fout)

    #FLIGHT NUMBER GENERATOR
    first_part = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
    last_part = ''.join(random.choice(string.digits) for _ in range(3))
    Flight_Number= first_part + last_part
    
    #SEAT NUMBER GENERATOR
    first_part = ''.join(random.choice(string.digits) for _ in range(2))
    last_part = ''.join(random.choice(string.ascii_uppercase) for _ in range(1))
    while True:
        try:
            if first_part=='00':
                raise ValueError
            else:
                SEAT= first_part + last_part
                break
        except ValueError:
            first_part = ''.join(random.choice(string.digits) for _ in range(2))

    #FROM the place
    FROM=input("ENTER PLACE OF DEPARTURE:")
    TO=input("ENTER PLACE OF ARRIVAL:")

    #DATE AND TIMINGS
    with open("FlightData.csv","r",newline="\r\n") as fin:
        obj=csv.reader(fin)
        available=[]
        for rec in obj:
            if rec[0]==FROM.upper() and rec[1]==TO.upper():
                available.append((rec[2],rec[3]))
        if len(available)==0:
            print("NO FLIGHTS AVAILABLE CURRENTLY.....TRY AGAIN LATER!....INCONVENIENCE REGRETTED")
            return

        print("Available Date and Timings:")
        count=1
        for i in available:
            print(count,'.',i)
            count+=1
        while True:
            try:
                choice=int(input("Enter your choice:"))
                DATE,TIMINGS=available[int(choice)-1]
                break
            except:
                print("Enter Valid Choice")
                
    #Passenger Details
    #NAME
    while True:
        try:
            PSNGR_NAME=input("ENTER PASSENGER'S NAME:")
            for char in PSNGR_NAME:
                if char.isalpha():
                    pass
                elif not char.isspace():
                    raise ValueError
            break
        except ValueError:
            print("!Enter Valid Name!")

    #AGE
    while True:
        try:
            PSNGR_AGE=input("ENTER PASSENGER'S AGE:")
            if PSNGR_AGE.isdigit()==True:
                break
            else:
                raise ValueError
        except ValueError:
            print("!ENTER VALID AGE!")

    #MOBILE NUMBER
    while True:        
        try:
            PSNGR_MOBNO=int(input("ENTER PASSENGER'S MOBILE NUMBER:"))
            break
        except ValueError:
            print("!ENTER VALID MOBILE NUMBER!")
    lst=[Flight_Number,SEAT,FROM.upper(),TO.upper(),TIMINGS,DATE,PSNGR_NAME.upper(),PSNGR_AGE,PSNGR_MOBNO]
    objct.writerow(lst)
    print("BOOKING IS SUCCESSFULLY DONE....HAPPY JOURNEY:)")
    List=["Flight Number","Seat Number","From","To","Timings","Date","Passenger Name","Passenger Age","Passenger Mobile Number"]
    i=0
    print("\nYOUR BOOKING DETAILS")
    while i<len(List):
        print(List[i],':',lst[i])
        i+=1
    fout.close()


#Generate Boarding pass 
def searchrecord():
    print("\n\t\t\t\tGENERATE BOARDING PASS")
    while True:
        try:
            FNO=input("Enter Flight Number:")
            if len(FNO)!=6:
                raise ValueError
            break
        except ValueError:
            print("Enter Valid Flight Number")
    
    while True:        
        try:
            MobNo=int(input("ENTER YOUR REGISTERED MOBILE NUMBER:"))
            break
        except ValueError:
            print("!ENTER VALID MOBILE NUMBER!")
        
    with open("flightrecord.csv","r",newline="\r\n") as fin:
        obj=csv.reader(fin)
        Found=False
        for rec in obj:
            if rec[0]==FNO.upper() and rec[8]==str(MobNo):
                Found=True
                print("=====================================================================================")
                print("\t\t\t\tDOMESTIC AIRLINES BOARDING PASS")
                print("=====================================================================================")
                print("Passenger Name:",rec[6],"\t\t\t\tFlight Number:",rec[0])
                print("From:",rec[2],"\t\t\t\t\tSeat Number:",rec[1])
                print("To:",rec[3],"\t\t\t\t\tTimings:",rec[4])
                print("=====================================================================================")
                print("\t\t\t\tHAVE A HAPPY AND SAFE JOURNEY :)")
                print("=====================================================================================")            
        if not Found:
            print("No such record found... Kindly check the details and try again") 

#Cancel Booking
def deleterecord():
    print("\n\t\t\t\tCANCEL A BOOKING")
    while True:
        try:
            FNO = input("Enter Flight Number:")
            if len(FNO) != 6:
                raise ValueError
            break
        except ValueError:
            print("Enter Valid Flight Number")

    while True:
        try:
            MNO = int(input("ENTER YOUR REGISTERED MOBILE NUMBER:"))
            break
        except ValueError:
            print("!ENTER VALID MOBILE NUMBER!")

    file = "flightrecord.csv"
    temp = "temp.csv"

    found = False
    with open(file, "r", newline="\r\n") as fin, open(temp, "w", newline="\r\n") as fout:
        reader = csv.reader(fin)
        writer = csv.writer(fout)
        for record in reader:
            if record[0] == FNO.upper() and record[8] == str(MNO):
                found = True
            else:
                writer.writerow(record)

    if found:
        os.remove(file)
        os.rename(temp, file)
        print("Booking canceled successfully.")
    else:
        print("Record not found.")


   
#Modify Passenger's information
def modifyrecord():
    print("\n\t\t\t\tMODIFY PASSENGER'S INFORMATION")
    while True:
        try:
            FNo = input("Enter Flight Number:")
            if len(FNo) != 6:
                raise ValueError
            break
        except ValueError:
            print("Enter Valid Flight Number")

    while True:
        try:
            MNo = int(input("ENTER YOUR REGISTERED MOBILE NUMBER:"))
            break
        except ValueError:
            print("!ENTER VALID MOBILE NUMBER!")

    file="flightrecord.csv"
    temp="temp.csv"
    data="FlightData.csv"
    with open(file, "r", newline="\r\n") as fin, open(temp, "w", newline="\r\n") as fout:
        reader = csv.reader(fin)
        writer = csv.writer(fout)
        Found = False

        for rec in reader:
            if rec[0] == FNo.upper() and rec[8] == str(MNo):
                Found = True
                FROM = rec[2]
                TO = rec[3]
                with open(data, "r", newline="\r\n") as dat:
                    readerobj = csv.reader(dat)
                    available = []
                    for row in readerobj:
                        if row[0]== FROM.upper() and row[1] == TO.upper():
                            available.append((row[2], row[3]))

                if len(available) == 0:
                    print("NO FLIGHTS AVAILABLE CURRENTLY TRY AGAIN LATER....INCONVENIENCE REGRETTED")
                    return

                print("Available Date and Timings:")
                count = 1
                for i in available:
                    print(count, '.', i)
                    count += 1

                while True:
                    try:
                        choice = int(input("Enter your choice:"))
                        DATE, TIMINGS = available[choice - 1]
                        rec[4] = TIMINGS
                        rec[5] = DATE
                        Found = True
                        #Generating new flight number and seat number
                        first_part = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
                        last_part = ''.join(random.choice(string.digits) for _ in range(3))
                        Flight_Number= first_part + last_part
                        rec[0]=Flight_Number

                        first_part = ''.join(random.choice(string.digits) for _ in range(2))
                        last_part = ''.join(random.choice(string.ascii_uppercase) for _ in range(1))
                        while True:
                            try:
                                if first_part=='00':
                                    raise ValueError
                                else:
                                    SEAT= first_part + last_part
                                    break
                            except ValueError:
                                first_part = ''.join(random.choice(string.digits) for _ in range(2))
                        rec[1]=SEAT
                        break
                    except:
                        print("Enter a valid choice")

            writer.writerow(rec)
            lst=rec

    if Found:
        os.remove(file)
        os.rename(temp,file)
        print("Record updated successfully.")
        List=["Flight Number","Seat Number","From","To","Timings","Date","Passenger Name","Passenger Age","Passenger Mobile Number"]
        i=0
        print("\nYOUR BOOKING DETAILS")
        while i<len(List):
            print(List[i],':',lst[i])
            i+=1
    else:
        print("Record not found. Please check your Flight Number and Mobile Number.")

    
      
            
           
#main menu
ch=0 
while ch!=6:
    print("\n\t\t\t\t  ^^ MAIN MENU ^^")
    print("----------------------------------------------------------------------------------------------")
    print("\t\t\t\t1. New Booking")
    print("\t\t\t\t2. Generate Boarding Pass")
    print("\t\t\t\t3. Cancel Booking")
    print("\t\t\t\t4. Modify Booking Details")
    print("\t\t\t\t5. Exit")
    try:
        ch=int(input("ENTER YOUR CHOICE:"))
        if ch==1:
            addrecord() 
        elif ch==2:
            searchrecord() 
        elif ch==3:
            deleterecord()           
        elif ch==4:
            modifyrecord()    
        elif ch==5:
            print("THANK YOU.....HAVE A NICE DAY :)")
            break
        else:
            print("!ENTER VALID CHOICE!")

    except ValueError:
        print("!ONLY VALID INPUT CHOICES ARE ALLOWED!")
