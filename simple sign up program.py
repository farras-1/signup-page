accounts = {}

print("========please signup your account========")
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
    print("password must containt one of the following : a-z ,A-Z ,and 0-9")
print("========please verify your account========")
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
