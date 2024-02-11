import os

def cambiar_nombres(ruta):
    # Obtener la lista de archivos en la ruta especificada
    archivos = os.listdir(ruta)

    # Iterar sobre cada archivo
    for archivo in archivos:
        # Construir la ruta completa del archivo
        ruta_completa_antigua = os.path.join(ruta, archivo)

        # Verificar si es un archivo (no es un directorio)
        if os.path.isfile(ruta_completa_antigua):
            # Reemplazar "." por "-"
            nuevo_nombre = archivo.replace(".", "-")

            # Agregar ".txt" al final
            nuevo_nombre = f"{nuevo_nombre}.txt"

            # Construir la ruta completa del nuevo archivo
            ruta_completa_nueva = os.path.join(ruta, nuevo_nombre)

            # Renombrar el archivo
            os.rename(ruta_completa_antigua, ruta_completa_nueva)

            print(f"Renombrado: {archivo} -> {nuevo_nombre}")

# Ruta del directorio que contiene los archivos a renombrar
ruta_directorio = "C:/Users/Lenovo/OneDrive/Desktop/python/RS_chicago_restaurants/entree_data/entree/session"

# Llamar a la función para cambiar los nombres de los archivos
cambiar_nombres(ruta_directorio)