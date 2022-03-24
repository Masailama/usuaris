import sqlite3


def run_sql(name, query, parameters=(), read=False):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    cursor.execute(query, parameters)
    conn.commit()
    data = cursor.fetchall()
    conn.close()
    if read:
        return data