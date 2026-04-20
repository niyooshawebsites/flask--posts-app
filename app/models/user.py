from app.extensions import mysql


def create_user(name, email, username, password):
    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)",
        (name, email, username, password),
    )
    mysql.connection.commit()
    cur.close()
    
def login_user(email):
    cur = mysql.connection.cursor()
    
    # get user by email
    result = cur.execute("SELECT * FROM users WHERE email = %s", [email])
    
    if result > 0:
        # get the stored hashed password
        data = cur.fetchone()
        password = data['password']
        
        return password
    else:
        return None
        
