import sqlite3

DB_PATH = "../db/lesson.db"


try:
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        conn.execute("PRAGMA foreign_keys = 1")
    # Task 1    
        query1 = """
        SELECT
        o.order_id,
        SUM(p.price * li.quantity) AS total_price
        FROM orders AS o
        JOIN line_items AS li
            ON o.order_id = li.order_id
        JOIN products AS p
            ON li.product_id = p.product_id
        GROUP BY o.order_id
        ORDER BY o.order_id
        LIMIT 5;
                """
        cursor.execute(query1)
        print(cursor.fetchall())
        
    # Task 2
        
        query2 = """
        SELECT
        c.customer_name,
        AVG(sub.total_price) AS average_total_price
        FROM customers c
        LEFT JOIN (
        SELECT
            o.customer_id AS customer_id_b,
            SUM(p.price * li.quantity) AS total_price
        FROM orders o
        JOIN line_items li
            ON o.order_id = li.order_id
        JOIN products p
            ON li.product_id = p.product_id
        GROUP BY o.order_id
         ) AS sub
        ON c.customer_id = sub.customer_id_b
         GROUP BY c.customer_id, c.customer_name;
        """  
        cursor.execute(query2)
        print(cursor.fetchall())     
        
     # task 3
        try:
            cursor.execute("""
            SELECT customer_id
            FROM customers
            WHERE customer_name = 'Perez and Sons'
            """)        
            customer_id = cursor.fetchone()[0]
            
            cursor.execute("""
            SELECT employee_id
            FROM employees
            WHERE first_name = 'Miranda' AND last_name = 'Harris'
            """)
            employee_id = cursor.fetchone()[0]
            
            cursor.execute("""
            SELECT product_id
            FROM products
            ORDER BY price ASC
            LIMIT 5
            """)
            product_ids = [row[0] for row in cursor.fetchall()]
            
            conn.execute("BEGIN")
            
            cursor.execute("""
                INSERT INTO orders (customer_id, employee_id, date)
                VALUES (?, ?, date('now'))
                RETURNING order_id
                """, (customer_id, employee_id))
            
            order_id = cursor.fetchone()[0]
            
            for pid in product_ids:
                cursor.execute("""
                    INSERT INTO line_items (order_id, product_id, quantity)
                    VALUES (?, ?, 10)
                    """, (order_id, pid))
            
            conn.commit()
            
            cursor.execute("""
                SELECT
                    li.line_item_id,
                    li.quantity,
                    p.product_name
                FROM line_items li
                JOIN products p
                    ON li.product_id = p.product_id
                WHERE li.order_id = ?
                """, (order_id,))
            print(cursor.fetchall())
            
        
        except sqlite3.Error as e:
            conn.rollback()
            print("Transaction failed:", e)
        # Task 4
        
        query4 = """
        SELECT
            e.employee_id,
            e.first_name,
            e.last_name,
            COUNT(o.order_id) AS order_count
        FROM employees e
        JOIN orders o
            ON e.employee_id = o.employee_id
        GROUP BY e.employee_id, e.first_name, e.last_name
        HAVING COUNT(o.order_id) > 5;
        """

        cursor.execute(query4)
        print(cursor.fetchall())
        

except sqlite3.Error as e:
    print(f"Database error: {e}")