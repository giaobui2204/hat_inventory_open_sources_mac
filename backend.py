from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from database import connect_db

app = FastAPI()

class Hat(BaseModel):
    name: str
    color: str
    size: str

import sqlite3  

@app.post("/hats/")
def add_hat(hat: Hat):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO hats (hat_name, hat_color, size) VALUES (?, ?, ?)", 
                   (hat.name, hat.color, hat.size))

    conn.commit()
    conn.close()

    return {"message": "Hat added successfully!"}

@app.get("/hats/")
def get_hats():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM hats")
    hats = [{"id": row[0], "name": row[1], "color": row[2], "size": row[3]} for row in cursor.fetchall()]
    conn.close()

    return hats

@app.put("/hats/{hat_id}")
def update_hat(hat_id: int, hat: Hat):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("UPDATE hats SET name=?, color=?, size=?", (hat.name, hat.color, hat.size))

    conn.commit()
    conn.close()

    return {"message": "Hat updated successfully"}

@app.delete("/hats/{hat_id}")
def delete_hat(hat_id: int):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM hats WHERE id=?", (hat_id,))

    conn.commit()
    conn.close()

    return {"message": "Hat deleted successfully"}
