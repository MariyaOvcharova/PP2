import psycopg2

podcluchenie = psycopg2.connect(
    host = 'localhost', 
    dbname = 'postgres',
    user='postgres',
    password='1234'
)

cursor = podcluchenie.cursor()

sql = """
    CREATE OR REPLACE PROCEDURE lolkek2(telep VARCHAR(16))
    AS
    $$ 
    BEGIN
        IF EXISTS (SELECT 1 FROM lolkek WHERE lolkek.telephone = telep) THEN
            DELETE FROM lolkek
            WHERE telephone = lolkek2.telep;
        END IF;
    END; $$

    LANGUAGE plpgsql;       
    """

telefon = input('Write telephone number:')
cursor.execute(sql)
podcluchenie.commit()
cursor.execute('CALL lolkek2(%s)', (telefon, ))
podcluchenie.commit()

