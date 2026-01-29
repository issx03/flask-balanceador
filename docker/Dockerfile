FROM python:3.11-slim

WORKDIR /app

# Copiamos la carpeta app completa al contenedor
COPY app /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Ejecutamos Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8000", "wsgi:app"]