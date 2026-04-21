from app.extensions import mysql

def create_post(title, content, author):
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO posts(title, content, author) VALUES(%s, %s, %s)", (title, content, author))
    
    mysql.connection.commit()
    cur.close()
    
def fetch_all_posts():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM posts")
    mysql.connection.commit()
    
    if result > 0:
        posts = cur.fetchall()
        cur.close()
        return posts
    else:
        cur.close()
        return None
        
    
    