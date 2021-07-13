import sqlite3
def connect(dbname):
    conn=sqlite3.connect(dbname)
    conn.execute("CREATE TABLE IF NOT EXISTS OYO_TABLE(NAME TEXT,ADDRESS TEXT,PRICE INT,AMINITIES TEXT)")
    print("Table created successfully")
    insert_sql="INSERT INTO OYO_HOTELS(NAME,ADDRESS,PRICE,AMENITIES)VALUES(?,?,?,?)"
    conn.execute(insert_sql,avlues)
    conn.commit()
    conn.close()
    def get_hotel_info(dbname):
        conn=sqlite3.connect(dbname)
        cur=conn.cursor()
        cur.execute("SELECT *FROM OYO_HOTELS")
        table_data=cur.fetchall()
        for record in table_data:
            print(record)
        conn.close()
