from mysql.connector import MySQLConnection, Error
from mysql_dbconfig import read_db_config

def connect():
    """ connect to mysql-database """

    db_config = read_db_config()
    conn = None

    try:

        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()

        if conn.is_connected():

            print('Connection established.')
            cursor.execute("SELECT * FROM country")
            row = cursor.fetchone()

            while row is not None:

                print(row)
                row = cursor.fetchone()
            

        else:
            print('Connection failed.')

    except Error as e:

        print(e)

    finally:

        if conn is not None and conn.is_connected():

            cursor.close()
            conn.close()
            print('Connection closed.')

def insert_stuff(country_data):
    """ connect to mysql-database """

    query = "INSERT INTO country(continent, name, geo_id) " \
            "VALUES(%s, %s, %s)"
    
    #single row
    #for .commit() args = (continent, name, geo_id)

    db_config = read_db_config()
    conn = None

    try:

        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()

        if conn.is_connected():

            print('Connection established.')
            cursor.executemany(query, country_data)

            """
            if u insert single row
            if cursor.lastrowid:
                print('last insert id', cursor.lastrowid)
            else:
                print('last insert id not found')
            """            

            conn.commit()

        else:
            print('Connection failed.')

    except Error as e:

        print(e)

    finally:

        if conn is not None and conn.is_connected():

            cursor.close()
            conn.close()
            print('Connection closed.')

if __name__ == '__main__':
    connect()

