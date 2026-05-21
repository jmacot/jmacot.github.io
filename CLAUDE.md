# CLAUDE.md

Este archivo orienta a Claude Code (claude.ai/code) para trabajar con este repositorio.

> **OBSOLETO (desde 2026-05):** este repo ya **no es el hub con login StatiCrypt**. Su `index.html` solo hace `<meta http-equiv="refresh">` a **`https://app.jmacot.com`**. Las herramientas viven ahora **gateadas (login Supabase) en `jmacot-app`** y servidas por Cloudflare Pages. **Todo lo descrito abajo (galería de cards, StatiCrypt, deploy GitHub Pages) es histórico.** Para trabajar en las tools, ir a `COT/jmacot-app/tools/<slug>/`. Ver `COT/CLAUDE.md` y `COT/jmacot-app/CLAUDE.md`.

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

## Login (StatiCrypt)

`password_template.html` se inyecta en el flujo de cifrado StatiCrypt vía
`.github/workflows/staticrypt-deploy.yml`. Diseño actual: **efecto "lamp"
sky→violet** sobre `#020617` (paleta fija oscura, coincide con accent line
del Sistema B y blobs cyan/violet del mesh de la landing → continuidad
visual al decryptar). Inspirado en Aceternity UI Lamp, adaptado a CSS puro
con `conic-gradient` + máscaras (sin framer-motion).

- **`password_preview.html`** es un mirror del template con stub que salta
  StatiCrypt (contraseña test `demo`). Se **regenera automáticamente** desde
  el template con `python3 tools/build-preview.py`. Tras editar
  `password_template.html`, ejecutar siempre el script (o
  `--check` para verificar sincronía sin escribir).
- **Placeholders StatiCrypt**: `/*[|template_title|]*/0`,
  `template_instructions`, `template_error`, `template_placeholder`,
  `template_toggle_show/hide`, `template_remember`, `template_button`,
  `js_staticrypt`, `is_remember_enabled`, `staticrypt_config`. NO renombrar
  ni borrar — los reemplaza StatiCrypt al cifrar.
- **IDs requeridos por el motor StatiCrypt**: `staticrypt_loading`,
  `staticrypt_content`, `staticrypt-form`, `staticrypt-password`,
  `staticrypt-remember`, `staticrypt-remember-label`, `error-msg`,
  `toggle-btn`, `icon-eye`, `icon-eye-off`.
- **No tiene dark/light toggle** — el efecto lamp solo funciona sobre
  fondo oscuro. Auto-theme JS eliminado del template.

### Animaciones diferidas (regla iOS Safari)

`#staticrypt_content` arranca con `class="hidden"` (display:none) y
StatiCrypt tarda varios cientos de ms en intentar auto-decrypt. Si las
animaciones se aplican directamente a los elementos, **iOS Safari las
consume durante ese periodo** y al hacerse visible el form aparece sin
transición.

Patrón obligatorio: animaciones bajo selector `body.animate .lamp-*`, y en
JS, justo tras `classList.remove("hidden")`:

```js
requestAnimationFrame(function() {
  document.body.classList.add('animate');
});
```

Aplica también al preview (en su DOMContentLoaded). Casos pasados de
"animación no se ve en móvil" siempre han sido este patrón.

## Desarrollo

```bash
npx serve -l 8088
```

Deploy: GitHub Pages desde `main`, raíz `/`.
