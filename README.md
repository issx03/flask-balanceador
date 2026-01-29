# Proyecto: Balanceo de Carga con NGINX y Flask

## Descripción del sistema

- El sistema consta de tres servidores backend idénticos (basados en **Flask** y servidos por **Gunicorn**) y un servidor **NGINX** que actúa como frontal.

- La función de NGINX aquí es doble: funciona como proxy inverso para proteger los servidores y como balanceador de carga, distribuyendo las peticiones de los usuarios entre las tres instancias (`web1`, `web2`, `web3`) usando el algoritmo _Round Robin_. 

- Todo el despliegue se gestiona de forma conjunta mediante un archivo de **Docker Compose**.

## Cómo arrancar el sistema

- Para poner todo en marcha, sitúate en la carpeta raíz del proyecto (donde está el `docker-compose.yml`) y lanza el siguiente comando en la terminal:

```bash
docker compose up --build -d
```

## Cómo probar el balanceo

- He verificado que el sistema funciona de tres formas diferentes:

    - **Script automatizado**: He incluido un script en `scripts/test_balanceo.sh`. Al ejecutarlo con `bash scripts/test_balanceo.sh`, verás cómo las respuestas van rotando entre los diferentes contenedores.

    - **En el navegador**: Si entras a http://localhost:8080 y recargas la página varias veces, verás cambiar el ID del host que te responde.

    - **Cabeceras**: Si inspeccionas el tráfico de red (F12), verás que las respuestas incluyen la cabecera personalizada X-Proxied-By: NGINX-Balanceador.

## Notas técnicas

- **Puertos**: El único puerto expuesto a mi máquina es el 8080. La comunicación con el puerto 8000 de Gunicorn ocurre solo dentro de la red privada de Docker.

- **Configuración NGINX**: Utilicé la directiva add_header para asegurar que la cabecera personalizada fuera visible desde el cliente.

- **Salud del sistema**: Los contenedores tienen configurado un healthcheck que revisa la ruta /status cada 10 segundos para asegurar que NGINX no envíe tráfico a una instancia caída.