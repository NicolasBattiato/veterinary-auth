# Imagen base
FROM python:3.12.7-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema (si son necesarias)
# Añadir las dependencias del sistema necesarias para que el servicio funcione
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiar el archivo de requerimientos primero (para aprovechar el cache)
COPY ./requirements.txt /app/requirements.txt

# Instalar las dependencias de Python
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copiar el código de la aplicación
COPY . /app

# Exponer el puerto
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
#ENTRYPOINT ["./docker/api/entrypoint.sh"]