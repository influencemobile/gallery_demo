import os
import sqlite3
from sqlite3 import Error


def create_connection():
    """ create a database connection to a database that resides
        in the memory
    """
    conn = None;
    cwd = os.getcwd()
    try:
        conn = sqlite3.connect(f'{cwd}\db\development.sqlite3')
        print(sqlite3.version)
        cur = conn.cursor()
        
        cur.execute('SELECT * FROM artists')
        [print(i) for i in cur.fetchall()]
        print('''


            
            ''')

        cur.execute('SELECT * FROM galleries')
        [print(i) for i in cur.fetchall()]
        print('''



            ''')
        cur.execute('SELECT * FROM paintings')
        [print(i) for i in cur.fetchall()]
        conn.commit()

        cur.close()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_connection()