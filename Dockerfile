# Usamos la versión oficial de Odoo 18 Community
FROM odoo:18

# Cambiamos a usuario root para instalar dependencias si fuera necesario
USER root

# Copiamos tus módulos personalizados al contenedor
# Nota: La carpeta extra-addons debe existir en tu repo
COPY ./extra-addons /mnt/extra-addons

# Volvemos al usuario odoo por seguridad
USER odoo

# Exponemos el puerto estándar de Odoo y el de Longpolling (chat/notificaciones)
EXPOSE 8069 8072
