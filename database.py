import os
import sqlite3

# Style issue: bad naming, no docstring
def getInfo_and_process(user_input, items):
    
    # Security issue (Critical): SQL Injection
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + user_input + "'"
    cursor.execute(query)
    user = cursor.fetchone()

    # Logic issue (Critical): Type concatenation error (str + int)
    count = 0
    message = "Total items: " + count
    print(message)

    # Performance issue (Warning): N+1 Query in loop
    results = []
    for item in items:
        cursor.execute("SELECT * FROM details WHERE item_id = ?", (item.id,))
        details = cursor.fetchall()
        results.append(details)

    # Logic issue (Warning): No None check
    print("User role: ", user.role)

    return results
