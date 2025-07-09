# Dockerfile
# Este archivo toma la imagen base de Bitnami y corrige los problemas
# de permisos y registro de usuario que causan errores de ejecución.
FROM bitnami/spark:3.5
# Cambiar al usuario root para poder modificar el sistema
USER root
# 1. Crear explícitamente el directorio HOME y la caché de Ivy para el usuario de Spark (uid 1001)
# 2. Asignar los permisos correctos a dicho usuario.
RUN mkdir -p /home/spark/.ivy2/local && \
 chown -R 1001:1001 /home/spark
# Registrar formalmente al usuario 'spark' en el sistema de usuarios del contenedor.
RUN echo "spark:x:1001:1001::/home/spark:/bin/bash" >> /etc/passwd
# Volver al usuario no-root por defecto para la ejecución de Spark
USER 1001
ENV HOME=/home/spark