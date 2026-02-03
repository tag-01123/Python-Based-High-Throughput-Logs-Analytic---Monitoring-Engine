from backend.config.sql_config import get_sql
from fastapi import Fastapi
app = Fastapi()

@app.post("/create_user/")
def creat_user(name,email,password):
    db=get_sql()
    cursor=db.cursor(dictionary=True)
    query="INSERT INTO users (name,email,password) VALUES (%s,%s,%s)"
    cursor.execute(query,(name,email,password))
    db.commit()
    cursor.close()
    db.close()
    return {"message":"User created successfully"}

@app.get("/get_users/") 
def get_users():
    db=get_sql()
    cursor=db.cursor(dictionary=True)
    query="SELECT * FROM users"
    cursor.execute(query)
    users=cursor.fetchall()
    cursor.close()
    db.close()
    return {"users":"users fetched successfully"}

@app.post("/update_users/")
def update_user(name,email,password):
    db=get_sql()
    cursor=db.cursor(dictionary=True)
    query="UPDATE users SET name=%s,email=%s,password=%s WHERE name=%s"
    cursor.execute(query,(name,email,password))
    db.commit()
    cursor.close()
    db.close()
    return {"message":"User updated successfully"}

@app.get("/delete_user/") 
def delete_user(name):
    db=get_sql()
    cursor=db.cursor(dictionary=True)
    query="DELETE FROM users WHERE name=%s"
    cursor.execute(query,(name,))
    db.commit()
    cursor.close()
    db.close()
    return {"message":"User deleted successfully"}