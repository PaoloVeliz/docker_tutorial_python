# Obtener o jalar una imagen del lenguaje que estan usando
FROM python:3-alpine

# CREAR UN FOLDER
WORKDIR /app

# Instalar las dependencias con el archivo
COPY requirements.txt ./


RUN pip install -r requirements.txt

COPY . .

EXPOSE 6000
CMD [ "flask", "run","--host","0.0.0.0","--port","6000"]