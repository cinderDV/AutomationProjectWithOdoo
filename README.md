# Proyecto de Automatización con Odoo 18

Este proyecto contiene una configuración de Odoo 18 con módulos personalizados, lista para desplegarse en Coolify mediante Docker Compose.

## Estructura del Proyecto

```
.
├── Dockerfile             # Dockerfile personalizado que incluye odoo.conf
├── docker-compose.yaml    # Configuración de Docker Compose
├── odoo.conf              # Archivo de configuración de Odoo
├── .env.example           # Ejemplo de variables de entorno
└── extra-addons/          # Módulos personalizados de Odoo
    ├── muk_web_theme/
    ├── muk_web_appsbar/
    ├── muk_web_chatter/
    ├── muk_web_colors/
    └── muk_web_dialog/
```

## Configuración en Coolify

### 1. Base de Datos PostgreSQL

Antes de desplegar Odoo, necesitas una base de datos PostgreSQL:

1. En Coolify, crea un nuevo servicio PostgreSQL (si aún no tienes uno)
2. Anota el nombre del servicio/host, usuario y contraseña
3. Si creas una base de datos dedicada para Odoo, anota el nombre

**Alternativa:** Odoo puede crear automáticamente la base de datos si le das acceso a PostgreSQL.

### 2. Variables de Entorno

Configura las siguientes variables de entorno en Coolify:

```env
HOST=nombre-del-servicio-postgres
USER=odoo
PASSWORD=tu_password_seguro_aqui
```

**Nota importante:**
- `HOST` debe ser el nombre del servicio de PostgreSQL en Coolify (o la IP si es externa)
- `USER` y `PASSWORD` son las credenciales de PostgreSQL
- Opcionalmente puedes agregar `DB_NAME` si quieres especificar la base de datos

### 3. Despliegue

1. Conecta tu repositorio Git en Coolify
2. Selecciona "Docker Compose" como tipo de despliegue
3. Configura las variables de entorno mencionadas arriba
4. Despliega el proyecto

**Nota:** El proyecto usa un Dockerfile personalizado que incluye el archivo `odoo.conf`. Coolify construirá automáticamente la imagen durante el despliegue.

### 3. Activar los Módulos Personalizados

Una vez desplegado Odoo:

1. Accede a tu instancia de Odoo en el navegador
2. Activa el "Modo Desarrollador":
   - Ve a Ajustes → Activar el modo de desarrollador
3. Actualiza la lista de aplicaciones:
   - Ve a Aplicaciones → Menú de tres puntos → Actualizar lista de aplicaciones
4. Busca e instala los módulos de MuK:
   - `muk_web_theme` (tema principal)
   - Los demás módulos se instalarán automáticamente como dependencias

## Módulos Incluidos

### MuK Web Theme
Tema moderno y personalizable para Odoo 18 que incluye:

- **muk_web_theme**: Tema principal con diseño moderno
- **muk_web_appsbar**: Barra lateral de aplicaciones
- **muk_web_chatter**: Mejoras en el sistema de mensajería
- **muk_web_colors**: Personalización de colores
- **muk_web_dialog**: Mejoras en los diálogos

## Agregar Nuevos Módulos

Para agregar nuevos módulos personalizados:

1. Coloca el módulo directamente en la carpeta `extra-addons/`
2. Asegúrate de que el módulo tenga la estructura correcta:
   ```
   extra-addons/
   └── tu_modulo/
       ├── __init__.py
       ├── __manifest__.py
       └── ... (otros archivos del módulo)
   ```
3. Haz commit y push al repositorio
4. Coolify desplegará automáticamente los cambios
5. Actualiza la lista de aplicaciones en Odoo

## Troubleshooting

### Los módulos no aparecen en Odoo

Si los módulos no aparecen en la lista de aplicaciones, sigue estos pasos:

1. **Ejecuta el script de diagnóstico en Coolify:**
   - Ve a tu aplicación en Coolify
   - Abre el terminal del contenedor (Console)
   - Ejecuta: `bash /diagnostic.sh` (si está disponible) o revisa manualmente:

2. **Verifica que los módulos estén montados:**
   ```bash
   ls -la /mnt/extra-addons/
   ```
   Deberías ver: `muk_web_theme`, `muk_web_appsbar`, `muk_web_chatter`, `muk_web_colors`, `muk_web_dialog`

3. **Verifica el archivo de configuración:**
   ```bash
   cat /etc/odoo/odoo.conf
   ```
   Debe contener: `addons_path = /usr/lib/python3/dist-packages/odoo/addons,/mnt/extra-addons`

4. **Revisa los logs del contenedor en Coolify:**
   - Ve a Logs en tu aplicación
   - Busca errores relacionados con "addons_path" o "extra-addons"
   - Verifica que no haya errores de permisos

5. **Si todo está correcto pero aún no aparecen:**
   - En Odoo, activa el Modo Desarrollador
   - Ve a Aplicaciones → Menú de tres puntos → Actualizar lista de aplicaciones
   - Busca "muk" en la barra de búsqueda
   - Si aún no aparecen, puede haber un error en los archivos `__manifest__.py` de los módulos

6. **Ejecutar diagnóstico manual:**
   Desde el terminal del contenedor en Coolify:
   ```bash
   find /mnt/extra-addons/ -name "__manifest__.py"
   ```
   Deberías ver 5 archivos `__manifest__.py` (uno por cada módulo)

### Error de permisos

Si hay errores de permisos:
- Verifica en Coolify que el volumen `./extra-addons` se está montando correctamente
- Los permisos de los archivos deben permitir lectura al usuario `odoo` dentro del contenedor

### Base de datos no conecta

Si Odoo no puede conectarse a la base de datos:
- Verifica que las variables de entorno `HOST`, `USER`, y `PASSWORD` estén configuradas en Coolify
- El `HOST` debería ser el nombre del servicio de PostgreSQL
- Si usas una base de datos externa, asegúrate de que sea accesible desde el contenedor

## Documentación Adicional

- [Documentación oficial de Odoo](https://www.odoo.com/documentation/18.0/)
- [Docker Hub - Imagen oficial de Odoo](https://hub.docker.com/_/odoo/)
- [Coolify Documentation](https://coolify.io/docs)
