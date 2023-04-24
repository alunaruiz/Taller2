# Taller2
Taller 2 - Topicos Avanzados en IA

INSTRUCCIONES
1. Opción a: ejecutar docker-compose
   Opción b: ejecutar minikube
   Estas opciones también están disponibles desde la máquina virtual de la universidad a través del acceso por VPN a las IP y puertos descritos.

2. Descargar y crear el set de datos para el proyecto:

Están en ejecución para revisión los servicios mencionados a continuación:

http://10.43.102.113:8501/docs 
 - Ejecutar /process_data
 - Se pueden observar los datos una vez procesados usando /Show Data
 (Se importan los datos, que son almacenados en la base de datos xdb)

3. Creación y entrenamiento del modelo:

http://10.43.102.113:8502/docs
 - Ejecutar /train_model
 (Se genera un nuevo modelo (Random Forest), entrenado a partir de los datos que residen en la base de datos xdb (tabla train_table) y se almacena este modelo en la ruta /home/estudiante/M_1/data/model.pkl)

4. Inferencia a partir del modelo

http://10.43.102.113:8503/docs
  - Ejecutar /predict
 (Se lee desde la base de datos zdb (tabla Temporal_Usuario), la data insertada por un usuario para inferencia del modelo, la cual es  procesada por model.pkl, generando una predicción)
