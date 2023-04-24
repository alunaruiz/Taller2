# Importar las bibliotecas necesarias
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression



def train_model(data):
    df = pd.DataFrame(data)  
    df = df.drop(df.columns[10], axis=1)
    df.columns = df.columns.astype(str)      

 
    # Obtener X e y a partir de los datos
    X = df.drop(df.columns[-5], axis=1)
    y = df.iloc[:, -5]
        
    # Dividir conjunto de datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
    # Crear el modelo de bosques aleatorios
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    
    # hacer predicciones
    y_pred = rf_model.predict(X_test)

    # calcular la precision
    accuracy = accuracy_score(y_test, y_pred)
    print('Precision del modelo:', accuracy)
    
    # Guardar modelo entrenado
    with open("../M_1/data/model.pkl", "wb") as f:
        pickle.dump(rf_model, f)
    print("Modelo entrenado guardado correctamente.")
    return accuracy

