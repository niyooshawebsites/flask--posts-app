from app.extensions import mysql


def create_user(name, email, username, password):
    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)",
        (name, email, username, password),
    )
    mysql.connection.commit()
    cur.close()
