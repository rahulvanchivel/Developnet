#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def passcheck(pg):
    if(pg>5):
        print("password used for 5 times to login change password to login again")
        input("enter the new password")
def passcheck(c):
    if(c>5):
        print("password used for 5 times to login change password to login again")
        input("enter the new password")
def encrption(a):
    pl=list(a)
    for i in range(len(a)):
        if(ord(pl[i])<121):
            pl[i]=chr(ord(pl[i])+2)
        else:
            if(ord(pl[i])==121):
                pl[i]='a'
            elif(ord(pl[i])==122):
                pl[i]='b'
    pll=''
    for i in pl:
        pll=pll+i
    print("password encrypted ",pll)


valid_cred = {
    'Rahul': 'py',
    'Dana': 'px',
    'Ram': 'pl',
    'Sam': 'pk',
    'Klen': 'pt'
}
c=0
def login():
    user_name = input("Enter your username: ")
    user_pass = input("Enter your password: ")
    if user_name in valid_cred and valid_cred[user_name] == user_pass:
        print("Access granted!!")
        encrption(user_pass)
        op=int(input("press 1 to login again"))
        if(op==0):
            login()
           
    else:
        print("Username or password is incorrect. Please register!!")
        print()
        a=int(input("To relogin press 1 or to create account press 0"))
        while(a):
            login()
           
        print("-----------Registration-----------")

        new_name = input("Enter a new username: ")
        print()
        new_pass = input("Enter a new password: ")
   
   
    #username = new_name
    #password = new_pass
        print("Registration complete. You can now Log In.")

login()  
op=int(input("press 0 to logout"))
if(op==0):
    login()


# In[ ]:


def trans(name):
    prev_acc= ['Rahul','Dana','Abhi','Lokesh','Brad']
    ka=input("Press 1 for transaction\nPress 2 for deposit\nPress 3 for withdrawl\nPress 4 to check balance\nPress 5 to print min statement") b      
    if(ka==2):
        am=input("Enter your account number")
        dep=input("Ënter the amount to be deposited" )
        print("Deposited Successfully!")
        if(name not in prev_acc):
            print('An amount of ₹25 has been deducted!!')
    elif(ka==1):
        am1=input("Enter your account number")
        amr=input("Enter the reciever's account number")
        tr=input("Enter the amount to be transfered")
        print("Transaction successfull!")
        if(name not in prev_acc):
            print('An amount of ₹25 has been deducted!!')
    elif(ka==4):
        am2=input("Enter your account number")
        tr1=input("Enter the amount to withdraw")
        print("Withdrawl successfull")
        if(name not in prev_acc):
            print('An amount of ₹25 has been deducted!!')
    

