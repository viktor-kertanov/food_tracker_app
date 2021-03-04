from flask import g
import sqlite3

def connect_db():
    sql = sqlite3.connect('/Users/viktorkertanov/Library/Mobile Documents/com~apple~CloudDocs/Личное/!LEARNING PYTHON/flask/food_tracker_app/food_tracker_db/foodtracker.db')
    sql.row_factory = sqlite3.Row
    return sql

# Checks global object g to check if sqlite3_db exists there. If not, then it connects to db and return the result
# of the connection
def get_db():
    if not hasattr(g,'sqlite3_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db