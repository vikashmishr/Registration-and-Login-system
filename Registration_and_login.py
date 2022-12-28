import re
import pandas as pd

try:
    df = pd.read_excel('login.xlsx',index_col=0)
except:
    df = pd.DataFrame()


def take_email():
    email = input('\n\nEnter email/username\n\n')
    if re.search(r'[a-zA-Z]+?.*@.+[.].+',email):
        return email
    elif email == '':
        print('\nClosing registration as no response received')
    else:
        print('''check your email/username:\n 
                    1. @ should be followed by .\n 
                    2. Should start with alphabet\n'''
                 )
        
        return take_email()


def take_password():
    password = input('\n\nEnter your password\n\n')
    if len(password)>5 and len(password)<16 and re.search(r'[A-Z]',password) and re.search(r'[a-z]',password) and re.search(r'[1-9]',password) and re.search(r'[^A-Za-z1-9]',password):
        return password
    else:
        print('''\nPassword must contain minimum\n
                 1. One special charater
                 2. One uppercase
                 3. One digit
                 4. One lowercase''')
        return take_password()



def registration():
    global df
    email = take_email()
    if email:
        password = take_password()
        df = pd.concat([df, pd.DataFrame([{'email':email,'password':password}])], ignore_index = True)
        print('\nRegistration successful')


def login():
    global df
    print('\nTo login please provide the details')
    email = take_email()
    try:
        if len(df[df['email']==email])==1:
            print('\nPlease provide password')
            password = take_password()
            if list(df[df['email']==email]['password'])[0]==password:
                print('\nLogin successful\n\n')
            else:
                print('\nThe password is incorrect')
                while True:
                    choice = input('\nchoose "forget password" or "retrieve password"\n\n')
                    if choice == 'retrieve password':
                        print('\nYour password is : ', list(df[df['email']==email]['password'])[0])
                        break
                    elif choice == 'forget password':
                        print('\nProvide a new password')
                        password = take_password()
                        a = df[df['email']==email].index[0]
                        df.loc[a,'password']=password
                        print('\nPassword entered successfully')
                        return login()
        else:
            print('\nYou are not registered yet')
            print('\nPlease register')
            registration()
    except:
        print('\nThere has been no registration yet')
        registration()


print('\nChoose out of the following: \n 1. For Registration: Register \n 2. For login: Login')

choice = input('Enter Register/Login\n\n')

if choice == 'Register':
    registration()
elif choice == 'Login':
    login()


with pd.ExcelWriter('login.xlsx', engine='openpyxl', mode='w') as writer:
    df.to_excel(writer, sheet_name="Sheet1" )
#     df.to_excel(writer, sheet_name='Technologies')
#     df2.to_excel(writer, sheet_name='Schedule')


