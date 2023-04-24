from fastapi import FastAPI
import mysql.connector
import csv

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/create-csv")
def create_csv():
    mydb = mysql.connector.connect(
        host="db",
        user="root",
        password="123456",
        database="estudiante_zdb_1"
    )
    cursor = mydb.cursor()

    cursor.execute("SELECT * FROM Temporal_Usuario")
    rows = cursor.fetchall()

    with open("./home/estudiante/F_1/data/covertype/covertype.train.csv", "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(rows)

    return {"Mensaje": "El archivo CSV se cargo con exito"}
    