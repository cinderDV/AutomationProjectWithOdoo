#!/bin/bash

echo "===== ODOO ADDONS DIAGNOSTIC ====="
echo ""

echo "1. Verificando contenido de /mnt/extra-addons:"
ls -la /mnt/extra-addons/
echo ""

echo "2. Verificando archivo odoo.conf:"
cat /etc/odoo/odoo.conf
echo ""

echo "3. Verificando permisos en extra-addons:"
ls -la /mnt/extra-addons/ | head -n 10
echo ""

echo "4. Verificando si los módulos tienen __manifest__.py:"
find /mnt/extra-addons/ -name "__manifest__.py" -type f
echo ""

echo "5. Verificando variables de entorno de la base de datos:"
echo "HOST: $HOST"
echo "USER: $USER"
echo "PASSWORD: [OCULTO]"
echo ""

echo "6. Verificando que Odoo pueda leer los módulos:"
ls -R /mnt/extra-addons/ | head -n 50
echo ""

echo "===== FIN DEL DIAGNÓSTICO ====="
