# 🚀 Inicio Rápido - Cliente Theme

## 📝 Resumen en 3 Pasos

### 1️⃣ Subir a Git y Hacer Deploy
```bash
git add extra-addons/cliente_theme
git commit -m "Add custom theme module with UI configuration"
git push origin main
```

Coolify detectará los cambios y reiniciará el contenedor automáticamente.

---

### 2️⃣ Instalar el Módulo en Odoo

1. Accede a tu contenedor:
   ```bash
   docker exec -it odoo_app bash
   ```

2. Actualiza la lista de módulos:
   ```bash
   odoo -u base -d nombre_de_tu_bd --stop-after-init
   exit
   ```

3. Reinicia el contenedor:
   ```bash
   docker restart odoo_app
   ```

4. Abre Odoo en el navegador
5. Ve a: `Aplicaciones`
6. Haz clic en: `Actualizar lista de aplicaciones`
7. Busca: `Cliente - Tema Personalizado`
8. Haz clic en: `Instalar`

---

### 3️⃣ Personalizar desde la Interfaz

1. Ve a: `Ajustes > General Settings`
2. Desplázate hasta la sección: `Cliente Theme`
3. Configura:
   - 📸 **Logo** (200x60 px, PNG)
   - 🌐 **Favicon** (16x16 px, ICO/PNG)
   - 🖼️ **Fondo de login** (1920x1080 px, JPG/PNG)
   - 🎨 **Colores** (usa el selector de color)
   - ✏️ **Textos** (nombre, títulos, footer)
4. Haz clic en: `Guardar`
5. Refresca el navegador: `Ctrl + Shift + R`

---

## ✅ ¡Listo!

Tu Odoo ahora tiene el branding personalizado del cliente **sin necesidad de editar código ni acceder al servidor**.

---

## 🔧 Troubleshooting

### Los cambios no se aplican
1. Limpia el caché: `Ctrl + Shift + R`
2. Reinicia el contenedor: `docker restart odoo_app`

### El módulo no aparece
1. Verifica que Coolify hizo el deploy
2. Ejecuta: `docker exec -it odoo_app odoo -u base -d tu_bd --stop-after-init`
3. Reinicia: `docker restart odoo_app`

### Error al subir imágenes
- Verifica el tamaño (máximo 2-3 MB por imagen)
- Usa formatos: PNG, JPG, ICO

---

## 📚 Más Información

Lee el `README.md` completo para detalles avanzados.
