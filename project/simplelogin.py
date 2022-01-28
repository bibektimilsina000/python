
# createdusername=0
# createdpassword=0

# usrusername=0
# usrpassword=0


def sinup ():
    print("Enter username and password to create accout")
 
    createdusername=input("username:")
    createdpassword=input("password:")
    print("accout created sucessfully")

def logintrue ():
    print("login now")

    usrusername=input("\n\nusername:")
    usrpassword=input("\n\n password:")
    print("login sucessful") 

def loginfalse():
    print("login failed \n please use valid username and password and try again")
 
    usrusername=input("\nusername :")
    usrpassword=input("\npassword :")
sinup()


if ((createdpassword == usrpassword) and (createdusername == usrusername)) :
    logintrue()

else:
    while True:
        loginfalse()