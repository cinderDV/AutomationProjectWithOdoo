# Proyecto de Automatización con Odoo 18

Este proyecto contiene una configuración de Odoo 18 con módulos personalizados, lista para desplegarse en Coolify mediante Docker Compose.

## Estructura del Proyecto

```
.
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

### 1. Variables de Entorno

Configura las siguientes variables de entorno en Coolify:

```env
HOST=db
USER=odoo
PASSWORD=tu_password_seguro_aqui
```

### 2. Despliegue

1. Conecta tu repositorio Git en Coolify
2. Selecciona "Docker Compose" como tipo de despliegue
3. Configura las variables de entorno mencionadas arriba
4. Despliega el proyecto

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

1. Verifica que el archivo `odoo.conf` esté correctamente montado
2. Asegúrate de que los módulos estén directamente en `extra-addons/`, no en subdirectorios
3. Verifica los logs del contenedor: `docker logs odoo_app`
4. Actualiza la lista de aplicaciones en modo desarrollador

### Error de permisos

Si hay errores de permisos, verifica que el contenedor tenga acceso de lectura a los archivos en `extra-addons/`.

## Documentación Adicional

- [Documentación oficial de Odoo](https://www.odoo.com/documentation/18.0/)
- [Docker Hub - Imagen oficial de Odoo](https://hub.docker.com/_/odoo/)
- [Coolify Documentation](https://coolify.io/docs)
