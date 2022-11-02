import mysql.connector

mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'blood_db')

mycursor = mydb.cursor()
while True:
    print("select an option from the menu")
    print('1 add donar')
    print('2 view all donar')
    print('3 search a donar')
    print('4 update a donar')
    print('5 delete a donar')
    print('6 exit')

    choice = int(input('Enter an option: '))
    if(choice==1):
        print('employee enter selected')
        
        name = input('enter the name: ')
        address = input('enter the address: ')
        
        
        phone = input('enter the phone number: ')
        total_blood_donated= input('enter the total blood donated: ')
        blood_group = input('enter the blood group: ')
        sql = 'INSERT INTO `blood_donater`(`Name`, `Phone_number`, `Address`, `total_blood_donated`, `blood_group`) VALUES (%s,%s,%s,%s,%s)'
        data = (name, address ,phone,total_blood_donated,blood_group)
        mycursor.execute(sql , data)
        mydb.commit()
    elif(choice==2):
        print('view blood')
        sql = 'SELECT * FROM `blood_donater`'
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)
    elif(choice==3):
        print('search a blood')
        blood_group = input('enter the blood group to be searched: ')
        
        sql = "SELECT `id`, `Name`, `Phone_number`, `Address`, `total_blood_donated`, `blood_group` FROM `blood_donater` WHERE `blood_group`='"+blood_group+"'"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)
    elif(choice==4):
        print('update the student')
        name = input('enter the name: ')
        address = input('enter the address: ')
        phone = input('enter the phone number: ')
        total_blood_donated= input('enter the total blood donated: ')
        #blood_group = input('enter the blood group: ')
    elif(choice==5):
        print('delete the student')
    elif(choice==6):
        break