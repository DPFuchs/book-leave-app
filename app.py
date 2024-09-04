from pwinput import pwinput
import string, random

# this function retrieves data from a text file 
def user(username, lvl, password, leave):
    # We're opening the text file with read permissions so we can store them individually in text files
    f = open("user.txt", "r") 
    #We need to loop through the text file line by line using a loop. 
    for i in f:
        #This allows to find the index of the seperator so we can slice the huge string that is in the format "Username@userlvl#password!Leave"
        pos = i.index("@") 
        #The information are being stored in lists 
        username.append(i[:pos])
        pos2 = i.index("#")
        lvl.append(i[pos+1:pos2])
        pos = i.rfind("!")
        password.append(i[pos2+1:pos])
        leave.append(int(i[pos+1:].strip("\n")))
    #This closes the file since it's contents are extracted
    f.close()

#This function checks if user's username and password matches with the actual user name and passwords extracted from the text file earlier. If it 
#matches then the function returns true or false if it doesn't
def login(user,password, lstUser, lstPass):
    for i in range(len(lstUser)):
        if user == lstUser[i] and password == lstPass[i]:
            print("Welcome", user)
            return True
    return False    

#This function returns the index of the user so the elements of the created lists can be accessed using the returned index 
def index(user, lstUser):
    for i in range(len(lstUser)):
        if user == lstUser[i]:
            return i

def lvl(lstlvl,u):
    if lstlvl[u] == "A":
        return Admin()
    if lstlvl[u] == "S":
        return Standard()
    
def Admin():
    print("------------------------------------")
    print("| Fuchs Inc. Leave Booking program |")
    print("|              Welcome             |")
    print("|       Press 1: Book leave        |")
    print("|       Press 2: Check Leave       |")
    print("|       Press 3: Add User          |")
    print("|       Press 4: Exit              |")
    print("------------------------------------")

def Standard():
    print("------------------------------------")
    print("| Fuchs Inc. Leave Booking program |")
    print("|              Welcome             |")
    print("|       Press 1: Book leave        |")
    print("|       Press 2: Check leave       |")
    print("|       Press 3: Exit              |")
    print("------------------------------------")

def AdminChoice(choice):
    if choice == 2:
        print(f"You have {lstLeave[u]} days left")
    elif choice == 3:
        CreateUser()
    elif choice == 4:
        print("Thank you for using our program")

def StandChoice(choice):
    if choice == 1:
        bookLeave(u, lstLeave)
    elif choice == 2:
        print(f"You have {lstLeave[u]} days left")
    elif choice == 3:
        print("Thank you for using our program")

#This function checks if the amount of days the user is trying to book is less than the amount of leave they have less. If it's valid then the 
#text file is updated
def bookLeave(u, lstLeave, book):
    if book > lstLeave[u]:
        print(f"You cannot book this amount of leave. Please note that you have {lstLeave[u]} leave days left")
    else:
        print("Sucessful")
        lstLeave[u] -= book
        Update(lstUser, lstPass, lstLvl, lstLeave, u)
        print(f"You have {lstLeave[u]} days left!")
    return lstLeave[u]

#This functin creates a new account by taking the users name, password and user level. Once the captcha is created, it's added to the file
def CreateUser():
    username = input("Enter name of user: ")
    passw = input("Enter the password: ")
    lvl = int(input("Enter 1 for an Admin User or Enter 2 for a standard user: "))
    if lvl == 1:
        s = "A"
    else:
        s = "S"
    while True:
        captcha = Captcha()
        print(captcha)
        cap = input("Enter the following captcha")
        if cap == captcha:
            break
        else:
            print("Wrong Captcha")
    f = open("user.txt", "a")
    f.write("\n")
    f.write(username+"@"+s+"#"+passw+"!"+ str(150))
    f.close()
    print("User Added!")
        
def Captcha():
    result = ""
    for i in range(6):
        #random indexes are passed as arguments through the chr function to create a random string 
        result += chr(random.randrange(65, 123))
    return result

def Update(user,passw,lvl, leave, u):
    temp = []
    f = open("user.txt", "r")
    # This loop copies the contents to a temp list
    for i in f:
        temp.append(i)
    f = open("user.txt", "w")
    #The lines that needs to be updated are changed and then added to the text file whilst everything else is added as is according to the temp
    for i in range(len(temp)):
        if i == u:
            f.writelines(user[u]+"@"+lvl[u]+"#"+ passw[u]+ "!" + str(leave[u]) + "\n")
        else:
            f.writelines(temp[i])
    f.close()

lstUser = []
lstLvl = []
lstPass = []
lstLeave = []

user(lstUser, lstLvl, lstPass, lstLeave)

attempts = 3

#This loop asks for user input and password and keeps asking for input until it's correct. There are three attempts allowed
while True:
    try:
        username = input("Enter user name: ")
        passw = pwinput("Enter your password: ", "*")
        if not login(username,passw,lstUser, lstPass) :
            print("Incorrect Login Credentials. Please try again")
        else:
            u = index(username, lstUser)
            break
        attempts -= 1
        print(f"{attempts} Left!")
        if attempts < 1:
            print(f"You are out of attempts")
            exit()    
    except (ValueError) and TypeError:
        print("Invalid Input")
        
login(username,passw,lstUser,lstPass)

lvl(lstLvl, u)

#This loop askes for the user to enter what aspect of the program they wish to use and the program acts per the choice 
while True:
    choice = int(input("What do you wish to do: "))
    try:
        if lstLvl[u] ==  "S":
            StandChoice(choice)
            if choice == 1:
                while True:
                    try:
                        book = int(input("Enter the number of days leave you wish to book or press 0 to exit: "))
                        if book == 0:
                            break
                        else:
                            bookLeave(u,lstLeave,book)
                            break
                    except (ValueError):
                        print("Invalid Input")
            elif choice == 3:
                break
        else:
            AdminChoice(choice)
            if choice == 1:
                while True:
                    try:
                        book = int(input("Enter the number of days leave you wish to book or press 0 to exit: "))
                        if book == 0:
                            break
                        else:
                            bookLeave(u,lstLeave,book)
                            break
                    except (ValueError):
                        print("Invalid Input")
            elif choice == 4:
                break
    except ValueError:
        print("Please enter a valid Number")