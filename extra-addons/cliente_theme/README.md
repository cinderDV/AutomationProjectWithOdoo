# 🎨 Cliente Theme - Módulo de Personalización Odoo 18.0

Módulo profesional para personalizar completamente la interfaz de Odoo 18.0 Community/Enterprise **desde la interfaz de Odoo** (sin necesidad de editar código).

## ✨ **Novedad: Configuración 100% desde la Interfaz**

**Ya NO necesitas editar archivos ni subir imágenes al servidor.** Todo se configura desde:

**Ajustes > General Settings > Cliente Theme**

## 📋 Características

### ✅ Nivel 1 - Assets (Branding Visual)
- ✅ **Panel de configuración visual** (Ajustes > Cliente Theme)
- ✅ **Logo del navbar** - Sube desde la interfaz
- ✅ **Favicon personalizado** - Sube desde la interfaz
- ✅ **Fondo de login** - Sube desde la interfaz
- ✅ **Colores corporativos** - Selector de color visual
- ✅ Variables SCSS personalizadas
- ✅ Estilos para formularios, vistas Kanban, tablas

### ✅ Nivel 2 - Estructura (Vistas XML)
- ✅ Modificación dinámica del navbar usando XPath
- ✅ Personalización de la pantalla de login
- ✅ Footer personalizado configurable
- ✅ Título personalizado de la pestaña del navegador
- ✅ Textos de bienvenida configurables

## 📂 Estructura del Módulo

```
cliente_theme/
├── __init__.py                      # Inicialización del módulo
├── __manifest__.py                  # Configuración y metadatos
├── README.md                        # Este archivo
├── static/
│   ├── description/
│   │   ├── README.md               # Guía para el icono del módulo
│   │   └── icon.png                # [AGREGAR] Icono del módulo (256x256)
│   ├── img/
│   │   ├── README.md               # Guía para las imágenes
│   │   ├── logo.png                # [AGREGAR] Logo del navbar (200x60)
│   │   ├── favicon.ico             # [AGREGAR] Favicon (16x16)
│   │   └── login_background.jpg    # [AGREGAR] Fondo de login (1920x1080)
│   └── src/
│       └── scss/
│           └── custom_theme.scss   # Variables SCSS y estilos personalizados
└── views/
    ├── webclient_templates.xml     # Personalización del navbar y layout
    └── login_templates.xml         # Personalización de la pantalla de login
```

## 🚀 Instalación en Docker + Coolify

### 1️⃣ **Verificar que el módulo está en el repositorio**

Asegúrate de que la carpeta `extra-addons/cliente_theme` esté en tu repositorio Git.

```bash
git status
git add extra-addons/cliente_theme
git commit -m "Add custom theme module"
git push origin main
```

### 2️⃣ **Coolify hará el deploy automáticamente**

Coolify detectará los cambios y reiniciará el contenedor de Odoo.

### 3️⃣ **Entrar al contenedor de Odoo**

```bash
docker exec -it odoo_app bash
```

### 4️⃣ **Actualizar la lista de aplicaciones**

Desde el contenedor:

```bash
odoo -u base -d nombre_de_tu_base_datos --stop-after-init
```

**Reemplaza** `nombre_de_tu_base_datos` con el nombre real de tu BD (ejemplo: `odoo_prod`).

### 5️⃣ **Instalar el módulo desde la interfaz de Odoo**

1. Abre Odoo en tu navegador
2. Ve a **Aplicaciones**
3. Haz clic en **Actualizar lista de aplicaciones** (icono de actualizar)
4. Busca **"Cliente - Tema Personalizado"**
5. Haz clic en **Instalar**

## ⚙️ Configuración y Personalización

### 🎨 **Personalizar TODO desde la Interfaz** (RECOMENDADO)

**No necesitas tocar código ni el servidor.** Sigue estos pasos:

1. **Inicia sesión en Odoo** como administrador

2. **Ve a**: `Ajustes > General Settings`

3. **Busca la sección**: `Cliente Theme`

4. **Configura lo que necesites**:
   - 📸 **Logo del navbar**: Haz clic en "Logo del Backend" y sube tu imagen (PNG, 200x60 px)
   - 🌐 **Favicon**: Sube el icono de la pestaña (ICO/PNG, 16x16 px)
   - 🖼️ **Fondo de login**: Sube la imagen de fondo (JPG/PNG, 1920x1080 px)
   - 🎨 **Color Primario**: Haz clic en el selector de color y elige tu color corporativo
   - 🎨 **Color Secundario**: Elige el color secundario
   - ✏️ **Textos**: Cambia el nombre de empresa, títulos, footer, etc.

5. **Guarda los cambios**: Haz clic en `Guardar`

6. **Refresca el navegador**: `Ctrl + Shift + R`

**¡Listo!** Todos los cambios se aplican automáticamente.

---

### 🎨 **Opción Avanzada: Cambiar Colores en SCSS** (opcional)

Si quieres ajustar estilos más allá de los configurables, edita:

`static/src/scss/custom_theme.scss`

```scss
$o-brand-primary: #1E40AF;        // Cambia este color
$o-brand-secondary: #10B981;      // Y este también
```

Luego actualiza el módulo:
```bash
docker exec -it odoo_app odoo -u cliente_theme -d nombre_bd --stop-after-init
```

## 🔄 Actualizar el Módulo Después de Cambios

### Si modificaste **archivos XML**:

```bash
docker exec -it odoo_app odoo -u cliente_theme -d nombre_de_tu_bd --stop-after-init
docker restart odoo_app
```

### Si modificaste **archivos SCSS/CSS**:

1. Actualiza el módulo:
   ```bash
   docker exec -it odoo_app odoo -u cliente_theme -d nombre_de_tu_bd --stop-after-init
   ```

2. Limpia el caché del navegador: `Ctrl + Shift + R`

3. Si no se aplican los cambios, reinicia el contenedor:
   ```bash
   docker restart odoo_app
   ```

## 🐛 Troubleshooting (Solución de Problemas)

### ❌ El módulo no aparece en la lista de aplicaciones

**Solución:**
```bash
docker exec -it odoo_app odoo -u base -d nombre_de_tu_bd --stop-after-init
docker restart odoo_app
```

### ❌ Los cambios de CSS no se aplican

**Soluciones:**
1. Limpia el caché del navegador (Ctrl + Shift + R)
2. Reinicia el contenedor: `docker restart odoo_app`
3. Verifica que el archivo SCSS esté en `__manifest__.py` → `assets`

### ❌ Error: "Module not found"

**Solución:**
- Verifica que la carpeta esté en: `extra-addons/cliente_theme/`
- Verifica que exista el archivo `__init__.py`
- Verifica que el volumen esté bien mapeado en `docker-compose.yaml`

### ❌ Las imágenes no se muestran

**Soluciones:**
1. Verifica que las rutas sean correctas: `/cliente_theme/static/img/logo.png`
2. Verifica que los archivos existan en la carpeta `static/img/`
3. Actualiza el módulo: `odoo -u cliente_theme -d nombre_bd --stop-after-init`
4. Reinicia el contenedor: `docker restart odoo_app`

## 📚 Próximos Pasos - Niveles Avanzados

### 🔹 Nivel 3 - Lógica de Interfaz (OWL Framework)
- Crear componentes reactivos personalizados
- Agregar botones personalizados a la barra de acciones
- Widgets personalizados en formularios

### 🔹 Nivel 4 - Reportes y Documentos (QWeb)
- Personalizar facturas PDF
- Personalizar presupuestos y albaranes
- Crear encabezados y pies de página corporativos

**¿Quieres implementar estos niveles?** Consulta con el desarrollador.

## 📞 Soporte

Para dudas o problemas, contacta al equipo de desarrollo.

## 📄 Licencia

LGPL-3 (Compatible con Odoo Community)

---

**Desarrollado para Odoo 18.0 Community/Enterprise**
**Entorno: Docker + Coolify + PostgreSQL 15**
