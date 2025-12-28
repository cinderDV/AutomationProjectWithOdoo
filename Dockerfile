FROM odoo:18.0

# Copiar el archivo de configuración personalizado
# La imagen base ya tiene el directorio /etc/odoo/
COPY --chown=odoo:odoo odoo.conf /etc/odoo/odoo.conf

# Copiar script de diagnóstico con permisos de ejecución
COPY --chmod=755 diagnostic.sh /diagnostic.sh

# El resto de la configuración viene del docker-compose.yaml
# - Volúmenes para extra-addons
# - Variables de entorno para la base de datos
