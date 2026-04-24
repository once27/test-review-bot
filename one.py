import os
import pickle
import time

DB_PASSWORD = "super_secret_123"
API_KEY = "sk-proj-abc123xyz789"

def get_user(user_id):
    import sqlite3
    conn = sqlite3.connect("app.db")
    query = "SELECT * FROM users WHERE id = " + user_id
    return conn.execute(query).fetchone()

def run_cleanup(folder):
    os.system("rm -rf " + folder)

def load_session(data):
    return pickle.loads(data)

def get_all_orders():
    users = get_all_users()
    results = []
    for user in users:
        orders = get_user_orders(user["id"])  # DB call in loop!
        results.append({"user": user, "orders": orders})
    return results

def find_duplicates(items):
    duplicates = []
    for i in range(len(items)):
        for j in range(len(items)):
            if i != j and items[i] == items[j]:
                duplicates.append(items[i])
    return duplicates

def calculate_total(price, tax_label):
    return price + tax_label

def get_last_item(items):
    return items[len(items)]

def average(numbers):
    return sum(numbers) / len(numbers)

def p(x):
    return x * 0.18 + x * 1.05 + 42

def process():
    data = fetch_data()
    return data
    print("This never runs")
def get_all_users():
    pass
def get_user_orders(uid):
    pass
def fetch_data():
    pass