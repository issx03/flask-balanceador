# Reflexión personal

1. ¿Qué has aprendido sobre balanceo de carga?

- He aprendido que el balanceo de carga es esencial para escalar aplicaciones horizontamente.

- Me ha permitido entender cómo un único punto de entrada (NGINX) puede gestionar grandes volúmenes de tráfico repartiendo la carga entre múltiples servidores backend, evitando cuellos de botella y asegurando que, si un servidor cae, el servicio siga funcionando.

2. ¿Cómo has verificado que el sistema funciona correctamente?

- He verificado el funcionamiento principalmente mediante el script `test_balanceo.sh`, observando en la terminal cómo las respuestas provenían de diferentes identificadores de contenedor de forma rotatoria.

- También he comprobado manualmente en el navegador la presencia de la cabecera personalizada y he simulado la caída de un nodo (`docker stop web2`) para confirmar que el tráfico se redirigía a los nodos restantes.

3. ¿Qué parte te ha resultado más difícil? ¿Por qué?

- Lo más complicado fue entender el comportamiento de los `healthchecks` al inicio. Al arrancar el sistema, el script de prueba devolvía siempre la misma instancia porque las otras aún no estaban marcadas como "saludables" por Docker.

- Tuve que comprender que existe un tiempo de arranque y verificación antes de que el balanceador empiece a rotar el tráfico correctamente.

4. ¿Qué harías diferente si tuvieras que repetirlo?

- Si tuviera que repetir la práctica, implementaría un script de prueba más robusto que verifique automáticamente el código de estado HTTP y la presencia de la cabecera personalizada, en lugar de solo imprimir el cuerpo de la respuesta.

- También exploraría configurar pesos diferentes en el bloque upstream de NGINX para simular servidores con distintas capacidades.

5. ¿Ves útil el uso de Gunicorn frente al servidor de desarrollo de Flask?

- Sí, es indispensable. El servidor integrado de Flask es monohilo y no está diseñado para seguridad o rendimiento en producción.

- Gunicorn permite manejar múltiples procesos de trabajo (workers) y gestionar conexiones concurrentes de manera eficiente, lo cual es vital cuando se pone una aplicación detrás de un balanceador de carga en un entorno real.
