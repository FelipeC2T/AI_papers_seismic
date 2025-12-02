# Guía de Deployment: Publicar el Informe HTML en Internet

## 🌐 Opciones de Hosting Gratuito

### Opción 1: GitHub Pages (Recomendado)

**Ventajas**: Gratis, permanente, dominio .github.io, versionado Git

#### Pasos:

1. **Crear cuenta en GitHub** (si no tienes)
   - Ir a https://github.com
   - Sign Up

2. **Crear nuevo repositorio**
   ```
   Nombre sugerido: seismic-ai-papers
   Public ✓
   NO inicializar con README (ya tenemos archivos)
   ```

3. **Subir archivos desde la terminal**:
   ```bash
   cd c:\Users\Felipe\Desktop\IA_papers
   
   # Inicializar Git
   git init
   
   # Agregar solo los archivos necesarios para la web
   git add index.html
   git add WEB_README.md
   
   # Renombrar README para GitHub
   git mv WEB_README.md README.md
   
   # Commit
   git commit -m "Informe inicial de papers de IA en interpretación sísmica"
   
   # Conectar con GitHub (reemplazar TU_USUARIO)
   git remote add origin https://github.com/Felipe_C2T/seismiAIpapers.git
   
   # Subir
   git branch -M main
   git push -u origin main
   ```

4. **Activar GitHub Pages**:
   - En tu repositorio en GitHub
   - Settings → Pages
   - Source: "Deploy from a branch"
   - Branch: main → / (root)
   - Save

5. **Tu sitio estará en**:
   ```
   https://TU_USUARIO.github.io/seismic-ai-papers/
   ```

---

### Opción 2: Netlify Drop (Más Fácil)

**Ventajas**: Super fácil, drag & drop, dominio .netlify.app

#### Pasos:

1. **Ir a**: https://app.netlify.com/drop

2. **Preparar archivos**:
   - Crear carpeta nueva llamada "web"
   - Copiar SOLO `index.html` a esa carpeta

3. **Drag & Drop**:
   - Arrastrar la carpeta "web" a la zona de Netlify Drop
   - Esperar que suba

4. **¡Listo!** Te dará una URL como:
   ```
   https://random-name-12345.netlify.app
   ```

5. **Personalizar dominio** (opcional):
   - Site settings → Change site name
   - Elegir nombre: `seismic-ai-papers`
   - URL final: `https://seismic-ai-papers.netlify.app`

---

### Opción 3: Vercel

**Ventajas**: Super rápido, buena integración con Git

#### Pasos:

1. **Ir a**: https://vercel.com

2. **Sign up** (puede ser con GitHub)

3. **New Project**:
   - Import Git Repository
   - O "Deploy" → subir carpeta

4. **Configuración**:
   - Framework Preset: Other
   - Build Command: (dejar vacío)
   - Output Directory: . (punto)

5. **Deploy**

6. **URL**: `https://proyecto.vercel.app`

---

### Opción 4: Render (Static Site)

**Ventajas**: Gratis, fácil, good performance

#### Pasos:

1. **Ir a**: https://render.com

2. **Sign Up** (con GitHub o email)

3. **New** → **Static Site**

4. **Conectar repositorio** o subir archivos

5. **Settings**:
   - Build Command: (vacío)
   - Publish Directory: . (punto)

6. **Create Static Site**

---

## 🚀 Método Rápido sin Git (Netlify)

Si quieres publicarlo AHORA mismo sin Git:

### Pasos Simplificados:

1. **Crear carpeta "deploy"** en el Desktop

2. **Copiar solo index.html** a esa carpeta

3. **Ir a**: https://app.netlify.com/drop

4. **Arrastrar la carpeta "deploy"** a la página

5. **¡LISTO!** - Tu sitio está en línea en segundos

---

## 📱 Compartir el Informe

Una vez publicado, puedes compartir la URL por:

- ✉️ Email
- 💬 WhatsApp / Telegram
- 📊 Presentaciones (insertar link)
- 📄 Documentos (como referencia)

---

## 🔧 Actualizar el Contenido

### Si usaste GitHub Pages:
```bash
# Editar index.html

git add index.html
git commit -m "Actualización del informe"
git push

# GitHub Pages se actualiza automáticamente en ~1 minuto
```

### Si usaste Netlify Drop:
- Simplemente arrastra nuevamente la carpeta
- Sobrescribirá el sitio anterior

---

## 🎨 Personalización Adicional

### Cambiar título o meta tags:

Editar en `index.html`:
```html
<title>Tu Título Personalizado</title>
<meta name="description" content="Tu descripción">
```

### Agregar analytics:

Insertar antes de `</body>`:
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

---

## ✅ Checklist de Deployment

- [ ] Revisar que `index.html` se vea bien localmente
- [ ] Elegir plataforma de hosting
- [ ] Subir archivos
- [ ] Verificar que funciona en el dominio público
- [ ] Probar en móvil
- [ ] Compartir URL con stakeholders

---

## 🆘 Solución de Problemas

### El sitio no carga:
- Verificar que el archivo se llame exactamente `index.html` (minúsculas)
- Esperar 1-2 minutos para que GitHub Pages se active

### Los estilos no se ven:
- Verificar que los estilos estén en el `<style>` tag dentro del HTML
- No hay archivos CSS externos que subir

### El sitio se ve mal en móvil:
- El HTML ya está optimizado con `<meta name="viewport">`
- Debería funcionar responsive automáticamente

---

## 💡 Recomendación Final

**Para uso inmediato**: Netlify Drop (5 minutos)  
**Para uso profesional a largo plazo**: GitHub Pages (10 minutos)

---

¿Necesitas ayuda? Los pasos más importantes son:
1. Ir a la plataforma elegida
2. Subir `index.html`
3. ¡Obtienes tu URL pública!
