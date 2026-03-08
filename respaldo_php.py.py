import os
import shutil
from datetime import datetime

origen = "C:\wamp64\www\web IA"
destino = "C:\\wamp64\\www\\Proyecto Final 1"

if not os.path.exists(destino):
    os.makedirs(destino)
for archivo in os.listdir(origen):
    if archivo.endswith(".php"):
        ruta_origen = os.path.join(origen, archivo)
        fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
        nuevo_nombre = f"{archivo.replace('.php','')}_{fecha}.php"
        ruta_destino = os.path.join(destino, nuevo_nombre)
        shutil.copy2(ruta_origen, ruta_destino)
        print(f"Archivo copiado y renombrado: {archivo} -> {nuevo_nombre}")

print("Proceso finalizado.")