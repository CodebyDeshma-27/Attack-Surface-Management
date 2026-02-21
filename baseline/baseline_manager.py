import sqlite3

DB_PATH = "baseline/baseline.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS baseline (
            host TEXT,
            port TEXT,
            protocol TEXT,
            service TEXT,
            version TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_baseline(scan_data):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("DELETE FROM baseline")

    for item in scan_data:
        cur.execute("""
            INSERT INTO baseline VALUES (?, ?, ?, ?, ?)
        """, (
            item["host"],
            item["port"],
            item["protocol"],
            item["service"],
            item["version"]
        ))

    conn.commit()
    conn.close()

def load_baseline():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM baseline")
    rows = cur.fetchall()
    conn.close()

    return [
        {
            "host": r[0],
            "port": r[1],
            "protocol": r[2],
            "service": r[3],
            "version": r[4]
        } for r in rows
    ]
