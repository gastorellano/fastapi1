# Hacer la siguiente importación de la clase:
from fastapi import FastAPI
# Instanciar la aplicación: 
app = FastAPI()
# Creamos nuestra función: 
@app.get('/') # esto llama la ruta raíz
def mensaje():
	return "¡Hola Mundo!"