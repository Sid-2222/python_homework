import sqlite3

try:
    with  sqlite3.connect("../db/magazines.db") as conn:
        print("Database connected successfully.")
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()
        
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS publishers(
                          name TEXT PRIMARY KEY NOT NULL 
                       )
                       """);
        
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS magazines(
                          name TEXT PRIMARY KEY NOT NULL,
                          publisher_name TEXT NOT NULL,
                          
                          FOREIGN KEY(publisher_name)
                          REFERENCES publishers(name)                          
                       )
                       """);
        
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS subscribers(
                          name TEXT PRIMARY KEY NOT NULL,
                          address TEXT NOT NULL                          
                       )
                       """);
        
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS subscriptions (
                          subscriber_name TEXT NOT NULL,
                          magazine_name TEXT NOT NULL, 
                          expiration_date TEXT NOT NULL, 
                          
                          FOREIGN KEY(subscriber_name)
                          REFERENCES subscribers(name),
                          
                          FOREIGN KEY(magazine_name)
                          REFERENCES magazines(name)                       
                       )
                       """);  
        # TABLES CREATED 
        
        def add_publisher(cursor, name):
            cursor.execute("SELECT name FROM publishers WHERE name = ?", (name,)) 
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO publishers(name) VALUES (?)" , (name,))
            else:
                print(f"Publisher '{name}' already exists.")
                
        def add_magazine(cursor,name,publisher_name):
            cursor.execute("SELECT name FROM magazines WHERE name = ?", (name,))
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO magazines(name, publisher_name) VALUES (?,?)" , (name,publisher_name))
            else:
                print(f"Magazine '{name}' already exists.")
                
        def add_subscriber(cursor,name,address):
            cursor.execute("SELECT * FROM subscribers WHERE name = ? AND address = ?", (name,address))
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO subscribers(name,address) VALUES(?,?)", (name,address))
            else:
                print(f"Subscriber '{name}' at '{address}' already exists.")
                
        def add_subscription(cursor, subscriber_name, magazine_name, expiration_date):
            cursor.execute("SELECT * FROM subscriptions WHERE subscriber_name  = ? AND magazine_name  = ?", (subscriber_name,magazine_name))
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO subscriptions(subscriber_name, magazine_name, expiration_date) VALUES (?, ?, ?)",(subscriber_name, magazine_name, expiration_date))
            else:
                print(f"{subscriber_name} is already subscribed to {magazine_name}.")
        
        # DEFINATIONS CREATED
        
        add_publisher(cursor,"Nat Geo")  
        add_publisher(cursor,"BBC") 
        add_publisher(cursor,"Momo B") 
        
        add_magazine(cursor,"Wild Journey","Nat Geo")
        add_magazine(cursor,"World Today", "BBC")
        add_magazine(cursor,"Food for Life", "Momo B")
        
        add_subscriber(cursor,"John Hammer","232 Div ave CA")
        add_subscriber(cursor,"Dosa Ross","909 Tele Rd CA")
        add_subscriber(cursor,"Momo Wiggly","552 Dog Park CA")
        
        
        add_subscription(cursor,"John Hammer","World Today","2027-01-01")
        add_subscription(cursor,"Dosa Ross","World Today","2027-01-01")
        add_subscription(cursor,"Dosa Ross","Food for Life","2027-06-01")
        add_subscription(cursor,"Momo Wiggly","Food for Life","2027-01-01")
        add_subscription(cursor,"Momo Wiggly","Wild Journey","2027-06-01")    
                   
    
        conn.commit()
        
        
        cursor.execute("SELECT * FROM subscribers")
        result = cursor.fetchall()
        for row in result:
            print(row)
        
        cursor.execute("SELECT * FROM magazines ORDER BY name")
        result = cursor.fetchall()
        for row in result:
            print(row)
            
        cursor.execute("""
                       SELECT magazines.name 
                       FROM magazines 
                       JOIN publishers
                       ON magazines.publisher_name = publishers.name
                       WHERE magazines.publisher_name = 'Momo B'
                       """)
        result = cursor.fetchall()
        for row in result:
            print(row)
            
            
    conn.close()
    print("Connection closed.")

except sqlite3.Error as e:
    print("SQLite error:", e)