import pandas as pd
import numpy as np
import mysql.connector
from fastapi import FastAPI

app = FastAPI()

@app.get("/process_data")
async def process_data():
    # Load data from folder
    df = pd.read_csv("../F_1/data/covertype/covertype.train.csv")

    # Dummy encode categorical variables
    df = pd.get_dummies(df, columns=["Soil_Type"])

    # Split data into three new dataframes
    n = len(df)
    train = df

    # Connect to MySQL database
    db = mysql.connector.connect(
        host="db_x",
        user="root",
        password="123456",
        database="xdb"
    )
    cursor = db.cursor()

    # Delete existing data from tables
    cursor.execute("DELETE FROM train_table")


    # Insert data into tables
    columns = ', '.join(train.columns)   
    placeholders = ', '.join(['%s']*len(train.columns))
    for i, row in train.iterrows():
        cursor.execute(f"INSERT INTO train_table ({columns}) VALUES ({placeholders})", tuple(row))


    # Commit changes and close database connection
    db.commit()
    db.close()

    return {"message": "Información procesada en base de datos xdb!"}

@app.get("/")
async def show_data():
    # Connect to MySQL database
    db = mysql.connector.connect(
        host="db_x",
        user="root",
        password="123456",
        database="xdb"
    )
    cursor = db.cursor()

    query = "SELECT * FROM train_table"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

    # Close database connection
    db.close()

    return {"message": "Información procesada y actualizada en base de datos xdb!"}