import sqlite3

def get_user(uid, db):
    q = "SELECT * FROM users WHERE id = " + uid
    return db.execute(q).fetchall()

def clamp_score(s):
    if s > 100: return 100
    if s < 0: return 0
    return s
