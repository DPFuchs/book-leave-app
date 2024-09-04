from pwinput import pwinput
import string, random

def user(username, lvl, password, leave):
    f = open("user.txt", "r")
    for i in f:
        pos = i.index("@")
        username.append(i[:pos])
        pos2 = i.index("#")
        lvl.append(i[pos+1:pos2])
        pos = i.rfind("!")
        password.append(i[pos2+1:pos])
        leave.append(int(i[pos+1:].strip("\n")))
    f.close()

def login(user,password, lstUser, lstPass):
    for i in range(len(lstUser)):
        if user == lstUser[i] and password == lstPass[i]:
            print("Welcome", user)
            return True
    return False    

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

def bookLeave(u, lstLeave, book):

    if book > lstLeave[u]:
        print(f"You cannot book this amount of leave. Please note that you have {lstLeave[u]} leave days left")
    else:
        print("Sucessful")
        lstLeave[u] -= book
        Update(lstUser, lstPass, lstLvl, lstLeave, u)
        print(f"You have {lstLeave[u]} days left!")
    return lstLeave[u]

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
    print("User Added!")
        
def Captcha():
    result = ""
    for i in range(6):
        result += chr(random.randrange(65, 123))
    return result

def Update(user,passw,lvl, leave, u):
    temp = []
    f = open("user.txt", "r")
    for i in f:
        temp.append(i)
    f = open("user.txt", "w")
    for i in range(len(temp)):
        if i == u:
            f.writelines(user[u]+"@"+lvl[u]+"#"+ passw[u]+ "!" + str(leave[u]) + "\n")
        else:
            f.writelines(temp[i])

lstUser = []
lstLvl = []
lstPass = []
lstLeave = []

user(lstUser, lstLvl, lstPass, lstLeave)

attempts = 3

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