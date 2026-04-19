# CLAUDE.md

Este archivo orienta a Claude Code (claude.ai/code) para trabajar con este repositorio.

## Proyecto

Landing page / hub central del ecosistema COT. Muestra una galería de herramientas clínicas organizadas por categoría (quirófano, administración, documentación, planificación). Cada card enlaza a una herramienta alojada en GitHub Pages.

## Sistema de diseño

Usa **Sistema A "Editorial"** (ver `../CLAUDE.md` y `../STYLE-GUIDE.md`):
- Fuentes: DM Serif Display + DM Sans + DM Mono (Google Fonts CDN)
- Header: gradiente premium `#0f172a → #1e293b` con glows sky/violet
- Cards: `border-radius: 20px`, barra de color `::before` 3px top, hover `translateY(-6px)`
- Colores por categoría: quirófano (sky), administración (violet), documentación (amber), planificación (teal)
- Dark mode: `[data-theme="dark"]` con sky toggle CSS puro

> **Nota:** Este archivo reemplaza la antigua guía de estilo duplicada que estaba aquí. La fuente de verdad para los sistemas de diseño es `COT/STYLE-GUIDE.md`.

## Arquitectura

App single-file (`index.html`). CSS en `<style>`, JS en `<script>`, sin build tools.

### Funciones JS clave

- `applyTheme(dark)` — aplica modo claro/oscuro al DOM y actualiza meta theme-color
- `getAutoTheme()` — auto-detecta dark mode por hora del sistema (21:00-07:00) y `prefers-color-scheme`
- `initTheme()` — inicializa tema al cargar; persiste en localStorage con expiración diaria

### Patrones únicos

- **Mesh gradient**: 5 blobs animados (cyan/violet/teal/pink/amber) con `filter: blur(80px)` + overlay dot grid
- **Sin autenticación propia**: las herramientas gestionan su propio auth vía `cot_auth` en localStorage
- **Stub localhost**: desactiva links de navegación externa en desarrollo local

## Desarrollo

```bash
npx serve -l 8088
```

Deploy: GitHub Pages desde `main`, raíz `/`.
