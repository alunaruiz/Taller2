import os
import mysql.connector
import pandas as pd
import joblib
from fastapi import FastAPI

# Configuracion de la aplicacion
app = FastAPI()
model_path = "../M_1/data/model.pkl"

# Definicion de rutas
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/predict")
async def predict():
    # Connect to MySQL database
    db = mysql.connector.connect(
        host="db_z",
        user="root",
        password="123456",
        database="zdb"
    )
    cursor = db.cursor()
    
    # Obtener datos de la base de datos
    cursor.execute("SELECT * FROM Temporal_Usuario")
    data = cursor.fetchone()

    # Convertir datos en DataFrame
    df = pd.DataFrame([data])
    columns = df.describe().columns.tolist()
    df.columns = columns
    print(columns)

    # Dummificar variables categoricas
    ##df = pd.get_dummies(df, columns=["Soil_Type","Wilderness_Area"])

    # Cargar modelo y hacer prediccion
    ##model = joblib.load(model_path)
    ##prediction = model.predict(df)

    # Retornar resultado
    ##return {"prediction": prediction[0]}
    
    db.close()

