import sqlite3
from sqlite3 import Connection

DB_NAME = 'sagraPOS.sqlite3'


# Get all menu entries of a specific menu
def selectMenuEntries(menuID):
    con = connectInitDB()
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    res = cur.execute('SELECT * FROM menuEntries WHERE ID = ?',
                      (menuID,)).fetchall()
    return [dict(row) for row in res]


# Get connection,
# initialize a new DB with the necessary tables if necessary
def connectInitDB() -> Connection:
    try:
        con = sqlite3.connect(f'file:{DB_NAME}?mode=rw', uri=True)
    except:
        print('No db found, initializing a new one')
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()
        print('New db created')
        # menus
        cur.execute('''
            CREATE TABLE "menus" (
            "ID"	INTEGER,
            "name"	TEXT NOT NULL,
            PRIMARY KEY("ID" AUTOINCREMENT));
            ''')
        print('Table menus created')
        # categories
        cur.execute('''
            CREATE TABLE "categories" (
	        "ID"	INTEGER,
	        "name"	TEXT NOT NULL,
	        PRIMARY KEY("ID" AUTOINCREMENT));
            ''')
        print('Table categorie created')
        # menuEntry
        cur.execute('''
            CREATE TABLE "menuEntries" (
                "ID"	INTEGER,
                "menuID"	INTEGER NOT NULL,
                "categoryID"	INTEGER,
                "name"	TEXT NOT NULL,
                "price"	REAL NOT NULL DEFAULT 0,
                "image"	BLOB,
                FOREIGN KEY("menuID") REFERENCES "menus"("ID") ON DELETE CASCADE,
                PRIMARY KEY("ID" AUTOINCREMENT),
                FOREIGN KEY("categoryID") REFERENCES "categories"("ID") ON DELETE SET NULL);
            ''')
        print('Table menuEntries created')

    return con
