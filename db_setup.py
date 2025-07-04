import sqlite3

conn = sqlite3.connect("job_data.db")
cursor = conn.cursor()

# Table create karenge
cursor.execute('''
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        company TEXT,
        location TEXT,
        tags TEXT,
        url TEXT,
        status TEXT DEFAULT 'Not Applied'
    )
''')

conn.commit()
conn.close()
print("✅ SQLite table created successfully!")
