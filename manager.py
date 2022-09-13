
from cryptography.fernet import Fernet
import mysql.connector
import keyring
import getpass
from os import system, name
import time



db = mysql.connector.connect(
    host= "localhost",
    user = "",
    passwd = "",
    auth_plugin='mysql_native_password',
    db = "pwdmanager"
    )

mycursor = db.cursor()

def clear():
  
    
    if name == 'nt':
        _ = system('cls')
  
    
    else:
        _ = system('clear')



def load_key():
    file = open("sqlpwd.key", "rb")
    key = file.read()
    file.close()
    return key
    
print("\n")    
print("*************** PASSWORD MANAGEMENT SYSTEM *******************")
print("*************** DESIGNED AND MAINTAINED BY *******************")  
print("********************** NAMAN NANDA ***************************")  
print("\n")
print("please enter the MASTER PASSWORD to access the PASSWORD MANAGER ")
master_pwd = getpass.getpass('enter the master password: ')
pwsss = keyring.get_password("passgenwsql","nimo")
if master_pwd == pwsss:
 print("WLECOME TO THE PASSWORD MANAGER")

 key = load_key() 
 fer = Fernet(key)

 def view():
    print("here are you PASSWORDS!!")
    print("\n")
    query=("select * from passwords")
    mycursor.execute(query)
    rows = mycursor.fetchall()    
    for r in rows:
        acc,user,password = r
        psw1 = fer.decrypt(password.encode()).decode()
        print("account: "+acc)
        print("username: "+user)
        print("password: "+psw1)
        print("\n")
        
        
  
 def add(user,password,account):
    password = fer.encrypt(password.encode()).decode()
    add_details = ("INSERT INTO passwords "
              "(accounts, name, password) "
              "VALUES (%s, %s, %s)")
    data_details= ( account,user,str(password))              
    mycursor.execute(add_details,data_details)
    db.commit()  
    print("PASSWORD ADDED!!")

 def update(gen_account,gen_user,gen_password):
    gen_password1 = fer.encrypt(gen_password.encode()).decode()
    general_details = ("UPDATE passwords "
                   "Set password = %s "
                   "WHERE accounts = %s and name = %s ")
    data_details = (gen_password1,gen_account,gen_user)                
    mycursor.execute(general_details,data_details)
    db.commit()
    print("PASSWORD UPDATED!!")
 def delete(passw,acco,usern):
    query=("select * from passwords where accounts = %s and name = %s")
    details = (acco,usern)
    mycursor.execute(query,details)
    rows = mycursor.fetchall()    
    for r in rows:
        acc,user,passwordq = r
        psw1 = fer.decrypt(passwordq.encode()).decode()   
    if psw1 == passw:
        query_new = ("DELETE from passwords where accounts = %s and name = %s")
        new_details = (acco,usern)
        mycursor.execute(query_new,new_details)
        db.commit()
        print("password DELETED!!")
    else:
        print("wrong account password, password not deleted!!")

 how = int(getpass.getpass("enter the Time: "))
 start_t = time.time()
 while time.time()-start_t <= how :

    mode = input("add a password, view your passwords, update, delete or press q to quit: ")
    mode_lower = mode.lower()

    if mode_lower == "q":
        break

    elif mode_lower == "add":
        account = input("enter the account: ")
        user = input("enter the username: ")
        pwd = getpass.getpass('enter the Password:')
        add(user, pwd, account)

    elif mode_lower == "view":
        view()   

    elif mode_lower == "update":
        account = input("enter the account which you want to update the password for: ")
        user = input("enter the username which you want to update the password for:  ")    
        new_password = getpass.getpass('enter the Password:')
        update(account,user,new_password)
    
    elif mode_lower == "delete":
        account = input("enter the account name you want to delete: ")
        user = input("enter the username of the account you want to delete: ")
        print("\n")
        print("\n")
        print("you'll need password to delete the account from the database")
        print("\n")
        print("without the password you won't be able to delete the account")
        print("\n")
        print("\n")
        password = getpass.getpass('enter the Password:')
        delete(password,account,user)

    else:
        continue
   
else:
    print("WRONG PASSWORD!!")


           
