# Práctica 11: Balanceo de Carga con Flask y NGINX

## Descripción del Sistema
Este proyecto implementa una arquitectura web escalable y de alta disponibilidad.
- **Backend:** 3 instancias de Flask servidas por Gunicorn (web1, web2, web3).
- **Frontend/Balanceador:** NGINX actuando como proxy inverso y balanceador de carga (Round Robin).
- **Infraestructura:** Todo containerizado con Docker y orquestado con Docker Compose.

## Despliegue
1. Clonar el repositorio.
2. Ejecutar `docker compose up --build -d`.
3. Acceder a `http://localhost:8080`.

## Pruebas
Se incluye un script en `scripts/test_balanceo.sh` que realiza 10 peticiones seguidas para demostrar cómo NGINX rota entre los contenedores disponibles.