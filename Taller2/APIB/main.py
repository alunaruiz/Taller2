import mysql.connector
import os
import shutil
import subprocess
from fastapi import FastAPI
import pickle
from app.model.train_model import train_model
import pandas as pd


app = FastAPI()

@app.get("/train_model")
async def get_data():
# Conexion a la base de datos MySQL
    db = mysql.connector.connect(
        host="db_x",
        user="root",
        password="123456",
        database="xdb"
    )
    cursor = db.cursor()

# Consulta a la base de datos
    cursor.execute("SELECT * FROM train_table")
    result = cursor.fetchall()
    cursor.close()
    db.close()

# Modelado
    # Copiar el script del modelo a un directorio temporal
    tmp_dir = "./tmp/model"
    if os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)
    shutil.copytree("./app/model", tmp_dir)

# Guardar result en un dataframe
    df = pd.DataFrame(result)
    # Aplicar la codificacion one-hot
    one_hot = pd.get_dummies(df[10])
    #Agregar las nuevas columnas al dataframe original
    df = pd.concat([df, one_hot], axis=1)
    # Entrenar el modelo
    old_accuracy = train_model(df)  
    # Evaluar si el nuevo modelo tiene mejor accuracy que el modelo existente
    #old_model_file = "./app/model/model.pkl"
    #new_model_file = f"{tmp_dir}/model.pkl"
    #old_accuracy = 0.8 # valor ficticio
    new_accuracy = 0.9 # valor ficticio
    if new_accuracy > old_accuracy:
        #Copiar los pesos del nuevo modelo al directorio del modelo
        #shutil.copy(new_model_file, old_model_file)
        print("El modelo actual sera reemplazado por el modelo nuevo")
    else:
        print("El modelo actual es mejor que el nuevo. No se haran cambios")
    
    # Eliminar el directorio temporal
    shutil.rmtree(tmp_dir)

    return {"message": "Modelo entrenado correctamente"}

