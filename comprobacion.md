# Verificaciones técnicas

1. ¿Qué función tiene el bloque `upstream` en NGINX?
   Define un grupo de servidores backend (en nuestro caso `web1`, `web2` y `web3`) bajo un nombre común (`flask_servers`). Esto permite a NGINX distribuir el tráfico entrante entre ellos usando algoritmos de balanceo como Round Robin.

2. ¿Qué cabecera personalizada has añadido?
   He añadido la cabecera `X-Proxied-By: NGINX-Balanceador` usando la directiva `add_header` en la configuración de NGINX para que sea visible en el navegador del cliente.

3. ¿Cuál es el propósito de los `healthcheck` en Docker Compose?
   Sirven para monitorizar el estado de los contenedores. Docker ejecuta periódicamente un comando (`curl` a `/status`); si falla varias veces, marca el contenedor como "unhealthy" (no saludable), lo que permite saber que esa instancia no está lista para recibir tráfico.

4. ¿Qué ocurre si una instancia de Flask se cae?
   Si una instancia cae (se detiene o falla el healthcheck), NGINX deja de enviarle tráfico y redistribuye las peticiones automáticamente entre las instancias restantes que siguen operativas, garantizando así la disponibilidad del servicio.

5. ¿Qué puerto usa NGINX y qué puertos usan las instancias Flask?
   - **NGINX:** Escucha en el puerto **80** interno del contenedor, mapeado al **8080** de mi máquina local (host).
   - **Flask/Gunicorn:** Cada instancia escucha en el puerto **8000** interno, que no está expuesto directamente al host, solo es accesible por NGINX dentro de la red de Docker.