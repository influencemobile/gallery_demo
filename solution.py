import os
import sqlite3
from sqlite3 import Error


def create_connection():
    """ create a database connection and return connection object """

    conn = None;
    cwd = os.getcwd()

    try:
        conn = sqlite3.connect(f'{cwd}\db\development.sqlite3')
        print(sqlite3.version)
        return conn

    except Error as e:
        print(e)

def insert_data(conn):
    """ Create 4 triggers 
    Trigger - Trigger Name
    UPDATE results ON INSERT IN artists - update_results_when_artist_inserted
    UPDATE results ON INSERT IN artists - update_results_after_artist_is_deleted
    UPDATE solutions ON INSERT IN paintings - update_solutions_when_painting_inserted
    UPDATE solutions ON DELETE IN paintings - update_solutions_after_painting_is_deleted
    """
    cur = conn.cursor()
        
    cur.execute('''CREATE TRIGGER IF NOT EXISTS update_results_when_artist_inserted
        AFTER INSERT ON artists
        BEGIN
            DELETE FROM results;

            INSERT INTO results (description, value, created_at, updated_at) VALUES ("Artists Average Age", (SELECT AVG(age) FROM artists), DATETIME(), DATETIME()),
            ("Artists Average Experience Level", (SELECT AVG(experience_level) FROM artists), DATETIME(), DATETIME());
        END;
        ''')
    conn.commit()

    cur.execute('''CREATE TRIGGER IF NOT EXISTS update_results_after_artist_is_deleted
        AFTER DELETE ON artists
        BEGIN
            DELETE FROM results;

            INSERT INTO results (description, value, created_at, updated_at) VALUES ("Artists Average Age", (SELECT AVG(age) FROM artists), DATETIME(), DATETIME()),
            ("Artists Average Experience Level", (SELECT AVG(experience_level) FROM artists), DATETIME(), DATETIME());
        END;
        ''')
    conn.commit()

    cur.execute('''CREATE TRIGGER IF NOT EXISTS update_solutions_when_painting_inserted
        AFTER INSERT ON paintings
        BEGIN
            DELETE FROM solutions;

            INSERT INTO solutions (description, painting, artist, gallery, created_at, updated_at)
            SELECT "Lowest Priced Painting",p.name, a.name, g.name, DATETIME(), DATETIME()
                FROM paintings p JOIN artists a ON p.artist_id = a.id
                JOIN galleries g ON p.gallery_id = g.id
                WHERE p.price = (SELECT MIN(price) FROM paintings)
            UNION
            SELECT "Highest Priced Painting",p.name, a.name, g.name, DATETIME(), DATETIME()
                FROM paintings p JOIN artists a ON p.artist_id = a.id
                JOIN galleries g ON p.gallery_id = g.id
                WHERE p.price = (SELECT MAX(price) FROM paintings)
            UNION
            SELECT "Median Priced Painting", p.name, a.name, g.name, DATETIME(), DATETIME()
                FROM paintings p JOIN artists a ON p.artist_id = a.id
                JOIN galleries g ON p.gallery_id = g.id
                WHERE p.price IN (SELECT price FROM paintings ORDER BY price 
                LIMIT (SELECT CASE WHEN COUNT(*)%2 = 0 THEN 2 ELSE 1 END FROM paintings) 
                OFFSET (SELECT CASE WHEN COUNT(*)%2 = 0 THEN COUNT(*)/2-1 ELSE COUNT(*)/2 END FROM paintings));
        END;
        ''')
    conn.commit()
        
    cur.execute('''CREATE TRIGGER IF NOT EXISTS update_solutions_after_painting_is_deleted
        AFTER DELETE ON paintings
        BEGIN
            DELETE FROM solutions;

            INSERT INTO solutions (description, painting, artist, gallery, created_at, updated_at)
            SELECT "Lowest Priced Painting",p.name, a.name, g.name, DATETIME(), DATETIME()
                FROM paintings p JOIN artists a ON p.artist_id = a.id
                JOIN galleries g ON p.gallery_id = g.id
                WHERE p.price = (SELECT MIN(price) FROM paintings)
            UNION
            SELECT "Highest Priced Painting",p.name, a.name, g.name, DATETIME(), DATETIME()
                FROM paintings p JOIN artists a ON p.artist_id = a.id
                JOIN galleries g ON p.gallery_id = g.id
                WHERE p.price = (SELECT MAX(price) FROM paintings)
            UNION
            SELECT "Median Priced Painting", p.name, a.name, g.name, DATETIME(), DATETIME()
                FROM paintings p JOIN artists a ON p.artist_id = a.id
                JOIN galleries g ON p.gallery_id = g.id
                WHERE p.price IN (SELECT price FROM paintings ORDER BY price 
                LIMIT (SELECT CASE WHEN COUNT(*)%2 = 0 THEN 2 ELSE 1 END FROM paintings) 
                OFFSET (SELECT CASE WHEN COUNT(*)%2 = 0 THEN COUNT(*)/2-1 ELSE COUNT(*)/2 END FROM paintings));
        END;
        ''')
    conn.commit()


    cur.close()

def close_connection(conn):
    if conn:
        conn.close()

if __name__ == '__main__':
    conn = create_connection()
    insert_data(conn)
    close_connection(conn)