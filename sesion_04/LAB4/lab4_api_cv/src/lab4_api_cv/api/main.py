from fastapi import FastAPI, UploadFile
import shutil
import os
from src.lab4_api_cv.services.image_service import analizar_imagen

app = FastAPI()

@app.post("/analyze-image")
def analyze_image(file: UploadFile):
    # Crear carpeta data si no existe
    if not os.path.exists("data"):
        os.makedirs("data")
        
    path = f"data/{file.filename}"
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    resultado = analizar_imagen(path)
    return {
        "mensaje": "Procesamiento exitoso",
        "resultado": resultado
    }