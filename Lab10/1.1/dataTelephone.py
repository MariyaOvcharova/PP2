import psycopg2
import csv
import os

podcluchenie = psycopg2.connect(
    host='localhost',
    dbname='postgres',
    user='postgres',
    password='1234'
)

cursor = podcluchenie.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS LOLKEK (
               first_name VARCHAR(50), 
               last_name VARCHAR(50),
               telephone VARCHAR(16) PRIMARY KEY
);""")

podcluchenie.commit()

print("Choose what would you do with information: insert from CSV or by yourself (BYS); change (CH); sorted (S); delete(D)")

var = input()

if var == 'CSV':
    print("Write name:")
    name = input()
    if os.access(name + '.csv', os.F_OK):
        with open(name + '.csv', 'r') as file:
            rfile = csv.reader(file)
            for i in rfile:
                first_name, last_name, telephone = i
                cursor.execute(f"SELECT * FROM LOLKEK WHERE telephone = '{telephone}'")
                existing_entry = cursor.fetchone()
                if existing_entry:
                    print(f'\033[91mPhone number {telephone} already exists!\033[0m')
                else:
                    cursor.execute("""INSERT INTO LOLKEK (first_name, last_name, telephone) VALUES (%s, %s, %s);""", (first_name, last_name, telephone))
                    podcluchenie.commit()
elif var.upper() == 'BYS':
    print("Write contacts:")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    telephone = input("Telephone: ")
    
    cursor.execute("""INSERT INTO LOLKEK (first_name, last_name, telephone) VALUES (%s, %s, %s);""", (first_name, last_name, telephone))
    podcluchenie.commit()

elif var.upper() == 'CH':
        ph = input("Enter the phone number: ")
        cursor.execute(f"SELECT * FROM LOLKEK WHERE telephone = '{ph}'")
        exist = cursor.fetchone()
        if exist:
            print('What you want to change? First Name(FN), LastName(LN), Telephone(T)')
            change = input()
            if change.upper() == 'FN':
                new_n = input(f"The current name is {exist[0]}, enter new one: ")
                cursor.execute(f"""UPDATE LOLKEK
                                SET first_name = '{new_n}'
                                WHERE telephone = '{ph}'
                                """)
                podcluchenie.commit()

            if change.upper() == 'LN':
                new_sn = input(f"The current name is {exist[1]}, enter new one: ")
                cursor.execute(f"""UPDATE LOLKEK
                                SET last_name = '{new_sn}'
                                WHERE telephone = '{ph}'
                                """)
                podcluchenie.commit()

            if change.upper() == 'T':
                new_t = input(f"The current telephone is {exist[2]}, enter new one: ")
                cursor.execute(f"""UPDATE LOLKEK
                                SET telephone = '{new_t}'
                                WHERE telephone = '{ph}'
                                """)
                podcluchenie.commit()
        else:
            print('Not found')

elif var.upper() == 'S':
        print('What you want to sort?')
        order = input()
        cursor.execute(f"""SELECT * FROM LOLKEK
                    ORDER BY {order} ASC;""")
        tab = cursor.fetchall()
        print("{:<29}{:<29}{:<29}".format("\033[94mName\033[0m", "\033[94mSurname\033[0m", "\033[94mPhone number\033[0m"))
        for val in tab:
            print("{:<20}{:<20}{:<20}".format(val[0],val[1], val[2]))
        print("")

elif var.upper() == 'D':
        print('Enter number')
        ph = input()
        cursor.execute(f"SELECT * FROM LOLKEK WHERE telephone = '{ph}'")
        existing_entry = cursor.fetchone()
        if existing_entry:
            cursor.execute(f"SELECT * FROM LOLKEK WHERE telephone = '{ph}'")
            deleted = cursor.fetchone()
            cursor.execute(f"DELETE FROM LOLKEK WHERE telephone = '{ph}'")
            podcluchenie.commit()
            print('Delited successfully')