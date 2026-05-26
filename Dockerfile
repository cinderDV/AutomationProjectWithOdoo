FROM odoo:18.0

# Parche para fix bug OrderedDict cron thread
USER root
RUN sed -i 's/for db_name, registry in registries.d.items():/for db_name, registry in list(registries.d.items()):/' /usr/lib/python3/dist-packages/odoo/service/server.py
USER odoo

# Copiar los addons personalizados directamente en la imagen
COPY --chown=odoo:odoo extra-addons /mnt/extra-addons

# Copiar el archivo de configuración personalizado
COPY --chown=odoo:odoo odoo.conf /etc/odoo/odoo.conf

# Copiar script de diagnóstico con permisos de ejecución
COPY --chmod=755 diagnostic.sh /diagnostic.sh

# Variables de entorno para la base de datos vienen del docker-compose.yaml
