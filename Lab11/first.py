import psycopg2

podcluchenie = psycopg2.connect(
    host = 'localhost', 
    dbname = 'postgres',
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

pattern = input()

find_pattern = f"""SELECT * FROM LOLKEK WHERE first_name LIKE '%' || '{pattern}' || '%'
OR last_name LIKE '%' || '{pattern}' || '%'
OR telephone LIKE '%' || '{pattern}' || '%'
"""

cursor.execute(find_pattern)

results = cursor.fetchall()

for row in results:
    print(row)
    

