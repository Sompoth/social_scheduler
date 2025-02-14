import sqlite3

DB_FILE = "scheduler.db"

def init_db():
    """Initialize the database and create the necessary table."""
    conn = sqlite3.connect(DB_FILE, check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS posts 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT, scheduled_time TEXT)''')
    conn.commit()
    return conn, cursor

def add_post(content: str, scheduled_time: str):
    """Insert a new post into the database."""
    conn, cursor = init_db()
    cursor.execute("INSERT INTO posts (content, scheduled_time) VALUES (?, ?)", (content, scheduled_time))
    conn.commit()
    conn.close()

def get_posts():
    """Retrieve all scheduled posts."""
    conn, cursor = init_db()
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    conn.close()
    return posts
