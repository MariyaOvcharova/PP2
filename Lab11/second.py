import psycopg2

podcluchenie = psycopg2.connect(
    host = 'localhost', 
    dbname = 'postgres',
    user='postgres',
    password='1234'
)

cursor = podcluchenie.cursor()

sql = """
    CREATE OR REPLACE PROCEDURE lolkek1(first_name VARCHAR(255), last_name VARCHAR(255), telep VARCHAR(16))
    AS
    $$ 
    BEGIN
        IF EXISTS (SELECT 1 FROM lolkek WHERE lolkek.telephone = telep) THEN
            UPDATE lolkek
            SET last_name = lolkek1.last_name, first_name = lolkek1.first_name
            WHERE telephone = lolkek1.telep;
        ELSE
            INSERT INTO lolkek VALUES
            (first_name, last_name, telep);
        END IF;
    END; $$

    LANGUAGE plpgsql;       
    """

user = input('User information:')
user_id = user.split()
cursor.execute(sql)
podcluchenie.commit()
cursor.execute('CALL lolkek1(%s, %s, %s)', (user_id[0], user_id[1], user_id[2]))
podcluchenie.commit()

