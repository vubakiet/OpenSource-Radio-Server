import psycopg2
import json


class Store:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="radio",
            user="postgres",
            password="admin"
        )

    def sql_database(self):
        cursor = self.conn.cursor()
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS tbl_music (id SERIAL PRIMARY KEY, name TEXT NOT NULL, image TEXT, path TEXT NOT NULL);')
        self.conn.commit()

    def delete_table(self):
        cursor = self.conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS tbl_music;')
        self.conn.commit()

    def add_music(self, name, image, path):
        cursor = self.conn.cursor()
        params = (name, image, path)
        cursor.execute(
            "INSERT INTO tbl_music (name, image, path) VALUES (%s, %s, %s);", params)
        self.conn.commit()
        print('Add Music Success !!!')

    def delete_music(self, id):
        cursor = self.conn.cursor()
        cursor.execute(
            "DELETE FROM tbl_music WHERE id = %s;", (id,))
        self.conn.commit()
        print('Delete Music Success !!!')

    def get_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM tbl_music;")
        return cursor.fetchall()

    def get_music_by_id(self, id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM tbl_music WHERE id = %s;", (id,))
        return cursor.fetchall()

    def get_music_last(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM tbl_music ORDER BY id DESC LIMIT 1")
        return cursor.fetchone()


# Create an instance of the Store class
store = Store()

# Call the necessary methods
store.sql_database()
store.add_music("name test 1", "image test 1", "path test 1")
store.add_music("name test 2", "image test 2", "path test 2")
store.delete_music(2)

data = store.get_all()
for item in data:
    print(item)

# Close the connection
store.conn.close()
