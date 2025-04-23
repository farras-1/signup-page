accounts = {}
def signup():
    try:
        user = input("please input your username :")
        while user == "":
            print("please fill the username")
            user = input("please input your username :")

        userpass = input("please input your password :")
        while userpass == "":
            print("please fill the password")
            userpass = input("please input your password :")

        accounts[user] = userpass
        print("account successfully created")
    except:
        print("account failed to create, please try again")

def login():
    
    userverif = input("please input your username :")
    while userverif == "":
        print("please fill your username")
        userverif = input("please input your username :")

    passverif = input("please input your password :")
    while passverif == "":
        print("please fill your password")
        passverif = input("please input your password :")

    if userverif in accounts and accounts[userverif] == passverif:
        print("account verification succeed")
    else:
        print("password or username incorrect")
        
while True:
    print("opsi :")
    print("sign up")
    print("login")
    print("keluar")

    opsi = input("masukkan opsi : ")

    if opsi == "sign up":
        signup()
    elif opsi == "login":
        login()
    elif opsi == "keluar":
        break
    else :
        print("opsi tidak valid")
