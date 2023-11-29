# Dockerfile para Django

FROM python:3.9

WORKDIR /app

# Copiar los archivos requerimientos y el código fuente al contenedor
COPY requirements.txt /app/
COPY . /app/

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto en el que se ejecutará la aplicación Django
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


