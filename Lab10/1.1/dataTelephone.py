import psycopg2

podcluchenie = psycopg2.connect(
    host = 'localhost',
    dbname = 'postgres',
    user = 'postgres',
    password = '1234'
)

cursor = podcluchenie.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS LOLKEK (
               first_name VARCHAR(50), 
               last_name VARCHAR(50),
               telephone VARCHAR(16) PRIMARY KEY

);""")

podcluchenie.commit()


print("Choose how you will insert informationt: from CSV or by yourself(BYS)")

var = input()

if var == 'CSV':
    print("Write path:")
    path = input()
    cursor.execute(f"""COPY LOLKEK(first_name, last_name, telephone)
                    FROM '{path}'
                    DELIMITER ','
                    CSV HEADER;
    """)
    podcluchenie.commit()
elif var.upper() == 'BYS':
    print("Write contacts:")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    telephone = input("Telephone: ")
    
    cursor.execute("""INSERT INTO LOLKEK(first_name, last_name, telephone)
                    VALUES (%s, %s, %s);
    """, (first_name, last_name, telephone))
    podcluchenie.commit()


