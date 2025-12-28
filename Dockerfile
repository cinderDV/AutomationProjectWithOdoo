FROM odoo:18.0

# Copiar el archivo de configuración personalizado
COPY odoo.conf /etc/odoo/odoo.conf

# Dar permisos apropiados
RUN chown odoo:odoo /etc/odoo/odoo.conf

# El resto de la configuración viene del docker-compose.yaml
# - Volúmenes para extra-addons
# - Variables de entorno para la base de datos
