#!/bin/bash
# Script de diagnóstico para Odoo en Coolify
# Ejecutar en el servidor SSH de Coolify

echo "=========================================="
echo "🔍 DIAGNÓSTICO DE DEPLOY - ODOO + COOLIFY"
echo "=========================================="
echo ""

# Colores
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 1. Verificar contenedor de Odoo
echo "1️⃣  Verificando contenedor de Odoo..."
ODOO_CONTAINER=$(docker ps --filter "ancestor=odoo:18.0" --format "{{.Names}}" | head -n 1)

if [ -z "$ODOO_CONTAINER" ]; then
    echo -e "${RED}❌ No se encontró contenedor de Odoo corriendo${NC}"
    echo "   Verifica en Coolify si el servicio está activo"
    exit 1
else
    echo -e "${GREEN}✅ Contenedor encontrado: $ODOO_CONTAINER${NC}"
fi
echo ""

# 2. Verificar última actualización del contenedor
echo "2️⃣  Verificando cuándo se creó el contenedor..."
CONTAINER_CREATED=$(docker inspect $ODOO_CONTAINER --format='{{.Created}}')
echo "   Creado: $CONTAINER_CREATED"
echo ""

# 3. Verificar si extra-addons está montado
echo "3️⃣  Verificando volumen /mnt/extra-addons..."
MOUNT_CHECK=$(docker exec $ODOO_CONTAINER ls /mnt/extra-addons 2>/dev/null)

if [ -z "$MOUNT_CHECK" ]; then
    echo -e "${RED}❌ /mnt/extra-addons está VACÍO o no existe${NC}"
    echo "   Problema: Coolify NO está montando el código"
    echo "   Solución: Verifica el docker-compose.yaml en Coolify"
    exit 1
else
    echo -e "${GREEN}✅ /mnt/extra-addons existe${NC}"
    echo "   Módulos encontrados:"
    docker exec $ODOO_CONTAINER ls -1 /mnt/extra-addons | sed 's/^/      - /'
fi
echo ""

# 4. Verificar si simple_theme existe
echo "4️⃣  Verificando si simple_theme está desplegado..."
SIMPLE_THEME=$(docker exec $ODOO_CONTAINER ls /mnt/extra-addons/simple_theme 2>/dev/null)

if [ -z "$SIMPLE_THEME" ]; then
    echo -e "${RED}❌ simple_theme NO está en el contenedor${NC}"
    echo "   Problema: Coolify no hizo pull del último commit"
    echo "   Solución: Haz redeploy manual en Coolify"
else
    echo -e "${GREEN}✅ simple_theme está desplegado${NC}"
    echo "   Archivos:"
    docker exec $ODOO_CONTAINER ls -1 /mnt/extra-addons/simple_theme | sed 's/^/      - /'
fi
echo ""

# 5. Verificar addons_path de Odoo
echo "5️⃣  Verificando configuración de Odoo (addons_path)..."
ADDONS_PATH=$(docker exec $ODOO_CONTAINER cat /etc/odoo/odoo.conf 2>/dev/null | grep "addons_path")

if [ -z "$ADDONS_PATH" ]; then
    echo -e "${YELLOW}⚠️  No se encontró odoo.conf${NC}"
else
    echo "   $ADDONS_PATH"
    if [[ $ADDONS_PATH == *"/mnt/extra-addons"* ]]; then
        echo -e "${GREEN}✅ Odoo SÍ está buscando en /mnt/extra-addons${NC}"
    else
        echo -e "${RED}❌ Odoo NO está buscando en /mnt/extra-addons${NC}"
        echo "   Problema: Falta agregar /mnt/extra-addons al addons_path"
    fi
fi
echo ""

# 6. Verificar último commit en GitHub
echo "6️⃣  Último commit en tu repositorio GitHub..."
echo "   (Revisa que coincida con lo que subiste)"
echo "   Ejecuta en tu máquina local:"
echo "   ${YELLOW}git log --oneline -1${NC}"
echo ""

# 7. Resumen
echo "=========================================="
echo "📊 RESUMEN"
echo "=========================================="

if [ -n "$SIMPLE_THEME" ] && [[ $ADDONS_PATH == *"/mnt/extra-addons"* ]]; then
    echo -e "${GREEN}✅ TODO CORRECTO - El módulo debería aparecer en Odoo${NC}"
    echo ""
    echo "Próximos pasos:"
    echo "1. Actualiza la lista de módulos:"
    echo "   docker exec $ODOO_CONTAINER odoo -u base -d TU_BD_NOMBRE --stop-after-init"
    echo ""
    echo "2. Reinicia el contenedor:"
    echo "   docker restart $ODOO_CONTAINER"
    echo ""
    echo "3. Abre Odoo > Aplicaciones > Actualizar lista > Busca 'Simple Backend Theme'"
else
    echo -e "${RED}❌ HAY PROBLEMAS - Revisa los errores arriba${NC}"
    echo ""
    echo "Soluciones:"
    if [ -z "$SIMPLE_THEME" ]; then
        echo "- Haz REDEPLOY en Coolify para que haga pull de Git"
    fi
    if [[ $ADDONS_PATH != *"/mnt/extra-addons"* ]]; then
        echo "- Agrega 'command: --addons-path=/usr/lib/python3/dist-packages/odoo/addons,/mnt/extra-addons' al docker-compose.yaml"
    fi
fi
echo ""
