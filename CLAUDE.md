# Guia de estilo — Herramientas Clinicas COT

> Referencia para crear nuevos archivos HTML consistentes con los proyectos existentes.

---

## 1. Vision general

**Autor:** jmacot (GitHub: github.com/jmacot) — Cirujano Ortopedico
**Arquitectura:** Single-file HTML (CSS en `<style>`, JS en `<script>`, sin frameworks)
**Hosting:** GitHub Pages en `https://jmacot.github.io/{repo}/`
**Idioma:** Siempre `lang="es"` (contenido en espanol)
**Hub central:** `jmacot.github.io` — landing page que enlaza a todas las herramientas

### Herramientas existentes

| Herramienta | Repo | Sistema | Categoria |
|-------------|------|---------|-----------|
| Calculadora de Guardias | calculadora-guardias | B | administracion |
| Material Externo | Material-Externo | B | documentacion |
| Plantillas Quirurgicas | plantillas-qx | B Premium | quirofano |
| CPAK Planner | CPAK | B | planificacion |
| Consentimientos Informados | consentimientos | A | documentacion |
| Landing Page (hub) | jmacot.github.io | A | — |

### Cuando usar cada sistema

- **Sistema A ("Editorial")** → Herramientas de navegacion, indices, documentos. El usuario lee y navega contenido.
- **Sistema B ("Clinico")** → Calculadoras, formularios, datos clinicos. El usuario introduce datos y obtiene resultados.
- **Sistema B Premium** → Variante de B con header degradado (patron A), category pills, panels glass, animaciones fadeInUp, dark mode, SVG icons. Para herramientas clinicas que necesitan estetica premium. Ejemplo: plantillas-qx.

---

## 2. Sistema de Diseno A — "Editorial/Elegante"

### Fuentes

```html
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Mono:wght@400;500&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet" />
```

- **Cuerpo:** `'DM Sans', sans-serif`
- **Titulos:** `'DM Serif Display', serif` (weight 400)
- **Labels/tags/mono:** `'DM Mono', monospace`

### Variables CSS

```css
:root {
  --bg: #f8fafc;
  --surface: #ffffff;
  --ink: #0f172a;
  --ink-muted: #64748b;
  --border: #e2e8f0;
  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.07), 0 2px 4px -2px rgb(0 0 0 / 0.07);
  --shadow-hover: 0 25px 50px -12px rgb(0 0 0 / 0.12);
  --radius: 20px;

  /* Colores vibrantes por categoria */
  --c-quirofano: #0ea5e9;       --c-quirofano-light: #e0f2fe;
  --c-administracion: #8b5cf6;  --c-administracion-light: #ede9fe;
  --c-documentacion: #f59e0b;   --c-documentacion-light: #fef3c7;
  --c-planificacion: #0d9488;   --c-planificacion-light: #ccfbf1;

  --transition-smooth: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}
```

### Rasgos clave

- **Header:** degradado premium `linear-gradient(135deg, #0f172a 0%, #1e293b 100%)`, glows `::before/::after` con `radial-gradient` + `filter: blur(40px)` (sky blue y violet)
- **Cards:** border-radius `var(--radius)` (20px), hover `translateY(-6px)` + shadow-hover + `border-color: var(--card-accent)`, barra `::before` de 3px en top, animacion `fadeInUp` escalonada
- **Cards estructura:** `.card-meta` (icono + SVG arrow) + `.card-content` (tag pill + h2 + p)
- **Arrow SVG:** circulo 32px con flecha `→`, en hover: fondo accent + `translateX(3px) scale(1.1)`
- **Botones filtro:** pill shape `border-radius: 999px`, DM Mono uppercase, activo con color de categoria
- **Footer:** DM Mono 11px, centrado, `border-top: 1px solid var(--border)`
- **h1:** `font-size: clamp(2rem, 5vw, 3.2rem)`
- **Transiciones:** `var(--transition-smooth)` con cubic-bezier suave

---

## 3. Sistema de Diseno B — "Clinico/Funcional"

### Fuentes

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Lora:wght@600;700&display=swap" rel="stylesheet">
```

- **Cuerpo:** `'Inter', Arial, sans-serif`
- **Titulos:** `'Lora', serif` (weight 600-700)

### Variables CSS

```css
:root {
  --bg: #f1f5f9;
  --surface: #ffffff;
  --surface2: #e8eef4;
  --border: #e2e8f0;
  --border-light: #e5e7eb;
  --accent: #1a3a5c;
  --accent-light: #eef2f7;
  --accent-hover: #14304f;
  --text: #222222;
  --text-muted: #555555;
  --text-light: #888888;
  --green: #16a34a;
  --green-light: #dcfce7;
  --amber: #c0540a;
  --amber-light: #fef3c7;
  --red: #dc2626;
  --red-light: #fee2e2;
  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.05);
  --shadow-hover: 0 20px 25px -5px rgb(0 0 0 / 0.1);
  --radius-sm: 8px;
  --radius: 16px;
  --radius-lg: 24px;
}
```

### Rasgos clave

- **Header (estandar):** centrado, sin fondo oscuro, h1 en `color: var(--accent)`
- **Header (premium):** degradado `linear-gradient(135deg, #0f2240 0%, #1a3a5c 50%, #234e77 100%)`, glows `::before/::after` con `radial-gradient` + `filter: blur(40px)`, h1 en blanco, subtitulo `rgba(255,255,255,0.6)`, border-radius `var(--radius-lg)` — usado en plantillas-qx
- **Cards:** border-radius `var(--radius)` (16px), `border: 1px solid var(--border-light)`, shadow upgrade en hover
- **Toggle buttons:** Controles segmentados estilo iOS — wrapper con fondo `--surface2`, padding 3px, radius 10px; boton activo con fondo `--surface` y `box-shadow: var(--shadow-sm)`
- **Category pills:** navegacion horizontal scrollable con `border-radius: 999px`, Inter 12px 600, activa con fondo `var(--accent)` + color blanco, badge con conteo — usado en plantillas-qx
- **Inputs:** `border: 1.5px solid var(--border)`, `border-radius: 8px`, focus: `box-shadow: 0 0 0 3px rgba(26,58,92,0.10)`
- **Labels:** 11px, `font-weight: 700`, uppercase, `letter-spacing: 0.5px`
- **Panels (estandar):** borde grueso `2px solid var(--accent)`, header con fondo solido `var(--accent-light)`
- **Panels (glass):** borde fino `1px solid var(--border)`, header con `backdrop-filter: blur(10px)` y fondo semi-transparente, iconos SVG inline en vez de emojis — usado en plantillas-qx
- **Textarea mono:** `'SF Mono', 'JetBrains Mono', 'Fira Code', 'Consolas', monospace` (preferido sobre `'Courier New'`)
- **Scrollbar custom:** `::-webkit-scrollbar` 6px, thumb rounded con `var(--accent-light)`
- **Back-button:** `position: fixed`, top 10px left 10px, `'SF Mono', 'Consolas', monospace`, `z-index: 100`
- **Toast:** purple `#7c3aed`, fixed bottom center, slide-up con `cubic-bezier(0.34, 1.56, 0.64, 1)`
- **Animaciones:** `fadeInUp` escalonada (header 0s, card 0.1s, panels 0.2s), `textFlash` al cargar contenido
- **Iconos:** SVG inline preferido sobre emojis para headers y botones (clipboard, bisturi, corazon)
- **Footer:** `font-size: 0.7rem`, `color: var(--text-light)`

---

## 4. Plantilla HTML base

### Template A (Editorial)

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{NOMBRE} · COT</title>
  <link rel="icon" type="image/svg+xml" href="icon.svg" />
  <link rel="apple-touch-icon" href="icon.svg" />
  <meta name="description" content="{DESCRIPCION}" />
  <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Mono:wght@400;500&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet" />
  <style>
    :root {
      --bg: #f8fafc;
      --surface: #ffffff;
      --ink: #0f172a;
      --ink-muted: #64748b;
      --border: #e2e8f0;
      --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
      --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.07), 0 2px 4px -2px rgb(0 0 0 / 0.07);
      --shadow-hover: 0 25px 50px -12px rgb(0 0 0 / 0.12);
      --radius: 20px;
      --transition-smooth: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'DM Sans', sans-serif; background: var(--bg); color: var(--ink); min-height: 100vh; }

    header {
      background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
      color: white; padding: 56px 48px 48px; position: relative; overflow: hidden;
    }
    header::before {
      content: ''; position: absolute; top: -150px; right: -50px;
      width: 400px; height: 400px; border-radius: 50%;
      background: radial-gradient(circle, rgba(14, 165, 233, 0.15) 0%, transparent 70%);
      filter: blur(40px);
    }
    header::after {
      content: ''; position: absolute; bottom: -120px; left: 20%;
      width: 350px; height: 350px; border-radius: 50%;
      background: radial-gradient(circle, rgba(139, 92, 246, 0.10) 0%, transparent 70%);
      filter: blur(40px);
    }
    .back-home {
      position: absolute; top: 16px; left: 16px;
      display: inline-flex; align-items: center; gap: 4px;
      font-family: 'DM Mono', monospace; font-size: 11px; letter-spacing: 0.05em;
      color: rgba(255,255,255,0.6); text-decoration: none;
      padding: 6px 12px; border-radius: 999px;
      border: 1px solid rgba(255,255,255,0.2); background: rgba(255,255,255,0.08);
      transition: border-color 0.2s, color 0.2s, background 0.2s; z-index: 1;
    }
    .back-home:hover { border-color: rgba(255,255,255,0.5); color: white; background: rgba(255,255,255,0.12); }
    .header-label {
      font-family: 'DM Mono', monospace; font-size: 11px;
      letter-spacing: 0.15em; text-transform: uppercase;
      color: rgba(255,255,255,0.5); margin-bottom: 16px;
    }
    header h1 {
      font-family: 'DM Serif Display', serif;
      font-size: clamp(2rem, 5vw, 3.2rem); font-weight: 400;
      line-height: 1.15; margin-bottom: 12px;
    }
    header p { font-size: 15px; color: rgba(255,255,255,0.65); font-weight: 300; max-width: 480px; }

    main { max-width: 900px; margin: 0 auto; padding: 56px 32px 80px; }
    footer {
      text-align: center; padding: 32px;
      font-family: 'DM Mono', monospace; font-size: 11px;
      color: var(--ink-muted); border-top: 1px solid var(--border);
    }
    footer a { color: var(--ink); text-decoration: none; }

    @media (max-width: 600px) {
      header { padding: 40px 24px 36px; }
      main { padding: 40px 20px 60px; }
      .back-home { padding: 4px 8px; font-size: 10px; top: 10px; left: 10px; }
    }
  </style>
</head>
<body>
  <header>
    <a class="back-home" href="https://jmacot.github.io/" title="Volver al inicio">← Inicio</a>
    <div class="header-label">{SECCION}</div>
    <h1>{TITULO}<br><em>{SUBTITULO}</em></h1>
    <p>{DESCRIPCION}</p>
  </header>
  <main>
    <!-- Contenido -->
  </main>
  <footer>
    <a href="https://github.com/jmacot" target="_blank">github.com/jmacot</a> · {ETIQUETA}
  </footer>
  <script>
    // JavaScript
  </script>
</body>
</html>
```

### Template B (Clinico)

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{NOMBRE}</title>
  <link rel="icon" type="image/png" href="icon.png">
  <link rel="apple-touch-icon" href="icon.png">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-title" content="{NOMBRE_CORTO}">
  <meta name="theme-color" content="#1a3a5c">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Lora:wght@600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #f1f5f9; --surface: #ffffff; --surface2: #e8eef4;
      --border: #e2e8f0; --border-light: #e5e7eb;
      --accent: #1a3a5c; --accent-light: #eef2f7; --accent-hover: #14304f;
      --text: #222222; --text-muted: #555555; --text-light: #888888;
      --green: #16a34a; --green-light: #dcfce7;
      --amber: #c0540a; --amber-light: #fef3c7;
      --red: #dc2626; --red-light: #fee2e2;
      --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
      --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.05);
      --shadow-hover: 0 20px 25px -5px rgb(0 0 0 / 0.1);
      --radius-sm: 8px; --radius: 16px; --radius-lg: 24px;
      --transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Inter', Arial, sans-serif; background: var(--bg);
      color: var(--text); min-height: 100vh; padding: 30px 20px;
      -webkit-tap-highlight-color: transparent;
    }
    input[type=number]::-webkit-inner-spin-button,
    input[type=number]::-webkit-outer-spin-button { -webkit-appearance: none; margin: 0; }
    input[type=number] { -moz-appearance: textfield; }

    .app-container { max-width: 900px; margin: 0 auto; }

    .back-home {
      position: fixed; top: 10px; left: 10px;
      display: inline-flex; align-items: center; gap: 4px;
      font-family: 'SF Mono', 'Consolas', monospace; font-size: 11px; letter-spacing: 0.05em;
      color: var(--text-muted); text-decoration: none;
      padding: 6px 12px; border-radius: 999px;
      border: 1.5px solid var(--border); background: var(--surface);
      box-shadow: 0 1px 4px rgba(0,0,0,0.08);
      transition: border-color 0.2s, color 0.2s; z-index: 100;
    }
    .back-home:hover { border-color: var(--accent); color: var(--accent); }

    .app-header { text-align: center; margin-bottom: 28px; }
    .app-header h1 {
      font-family: 'Lora', serif; color: var(--accent);
      font-size: clamp(1.3rem, 3vw, 1.7rem); font-weight: 700;
    }
    .app-header p { font-size: 13px; color: var(--text-muted); }

    .app-footer { text-align: center; flex-shrink: 0; padding: 8px 0; }
    .app-footer span { font-size: 0.7rem; color: var(--text-light); letter-spacing: 0.03em; }

    .toast-banner {
      position: fixed; bottom: 24px; left: 50%;
      transform: translateX(-50%) translateY(80px);
      background: #7c3aed; color: white;
      padding: 12px 28px; border-radius: 10px;
      font-size: 0.95rem; font-weight: 600;
      font-family: 'Inter', Arial, sans-serif;
      box-shadow: 0 8px 32px rgba(124,58,237,0.30);
      z-index: 9999; opacity: 0;
      transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1), opacity 0.4s;
      pointer-events: none; display: flex; align-items: center; gap: 8px;
    }
    .toast-banner.show { opacity: 1; transform: translateX(-50%) translateY(0); }

    @media (max-width: 600px) {
      .back-home { padding: 4px 8px; font-size: 10px; top: 6px; left: 6px; }
    }
  </style>
</head>
<body>
<div class="app-container">
  <a class="back-home" href="https://jmacot.github.io/" title="Volver al inicio">← Inicio</a>
  <div class="app-header">
    <h1>{TITULO}</h1>
    <p>{DESCRIPCION}</p>
  </div>

  <!-- Contenido -->

  <div class="app-footer"><span>COT — {NOMBRE} v1.0</span></div>
  <div id="toast" class="toast-banner"></div>
</div>
<script>
  // ─────────────────────────────────────────────
  //  TOAST
  // ─────────────────────────────────────────────
  function mostrarToast(msg) {
    const t = document.getElementById('toast');
    t.textContent = msg;
    t.classList.add('show');
    clearTimeout(t._timer);
    t._timer = setTimeout(() => t.classList.remove('show'), 2200);
  }
</script>
</body>
</html>
```

---

## 5. Biblioteca de componentes

### Card (Sistema A)

```css
.card {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: 16px; padding: 32px;
  text-decoration: none; color: inherit;
  display: flex; flex-direction: column; gap: 16px;
  box-shadow: var(--shadow);
  transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
  position: relative; overflow: hidden;
}
.card:hover { transform: translateY(-3px); box-shadow: var(--shadow-hover); border-color: transparent; }
.card::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0;
  height: 3px; background: var(--card-accent); border-radius: 16px 16px 0 0;
}
.card h2 { font-family: 'DM Serif Display', serif; font-size: 1.4rem; font-weight: 400; }
.card p { font-size: 14px; color: var(--ink-muted); line-height: 1.65; }
.card-tag {
  font-family: 'DM Mono', monospace; font-size: 10px; letter-spacing: 0.1em;
  text-transform: uppercase; padding: 4px 10px; border-radius: 999px;
  color: var(--card-tag-color); background: var(--card-tag-bg);
}
.card-icon {
  width: 48px; height: 48px; border-radius: 12px;
  background: var(--card-icon-bg);
  display: flex; align-items: center; justify-content: center; font-size: 22px;
}
```

### Card (Sistema B)

```css
.card {
  background: var(--surface); border: 1px solid var(--border-light);
  border-radius: var(--radius); box-shadow: var(--shadow);
  padding: 16px 20px;
}
.card:hover { box-shadow: var(--shadow-hover); }
```

### Formularios (Sistema B)

```css
.form-row { display: flex; gap: 16px; align-items: center; flex-wrap: wrap; }
.form-group { display: flex; flex-direction: column; }
.form-group label {
  font-size: 11px; font-weight: 700; color: var(--text-muted);
  text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 4px;
}
.form-group input, .form-group select {
  border: 1.5px solid var(--border); border-radius: 8px;
  padding: 14px 18px; font-size: 16px;
  font-family: 'Inter', Arial, sans-serif; color: var(--text);
  background: var(--surface); transition: border-color 0.2s, box-shadow 0.2s;
}
.form-group input:focus, .form-group select:focus {
  outline: none; border-color: var(--accent);
  box-shadow: 0 0 0 3px rgba(26,58,92,0.10);
}

@media (max-width: 600px) {
  .form-row { flex-direction: column; }
  .form-group { width: 100%; }
  .form-group input, .form-group select { width: 100% !important; }
}
```

### Botones (Sistema B)

```css
.btn-primary {
  background: var(--accent); color: white; border: none;
  border-radius: 8px; padding: 8px 24px; font-size: 13px; font-weight: 700;
  cursor: pointer; transition: all 0.2s; font-family: 'Inter', Arial, sans-serif;
}
.btn-primary:hover { background: var(--accent-hover); box-shadow: var(--shadow-hover); transform: translateY(-1px); }
.btn-primary:active { transform: translateY(0); }

.btn-green {
  background: var(--green); color: white; border: none;
  border-radius: 8px; padding: 8px 24px; font-size: 13px; font-weight: 700;
  cursor: pointer; transition: all 0.2s;
}
.btn-green:hover { background: #15803d; transform: translateY(-1px); }

.btn-danger {
  background: transparent; color: #dc2626; border: 1.5px solid #dc2626;
  border-radius: 8px; padding: 8px 18px; font-size: 13px; font-weight: 700;
  cursor: pointer; transition: all 0.2s;
}
.btn-danger:hover { background: #dc2626; color: white; }
```

### Botones pill (Sistema A)

```css
.filter-btn {
  font-family: 'DM Mono', monospace; font-size: 11px;
  letter-spacing: 0.08em; text-transform: uppercase;
  padding: 7px 16px; border-radius: 999px;
  border: 1.5px solid var(--border); background: transparent;
  color: var(--ink-muted); cursor: pointer; transition: all 0.2s;
}
.filter-btn:hover { border-color: var(--ink-muted); color: var(--ink); }
.filter-btn.active { border-color: transparent; color: white; background: var(--ink); }
```

### Panels dos columnas — estandar (Sistema B)

```css
.panels-grid {
  display: grid; grid-template-columns: 1fr 1fr; gap: 14px; flex: 1; min-height: 0;
}
.panel {
  background: var(--surface); border: 2px solid var(--accent);
  border-radius: var(--radius); box-shadow: var(--shadow);
  display: flex; flex-direction: column; overflow: hidden; transition: box-shadow 0.3s;
}
.panel:hover { box-shadow: var(--shadow-hover); }
.panel-header {
  display: flex; align-items: center; justify-content: space-between;
  padding: 10px 16px; background: var(--accent-light);
  border-bottom: 2px solid var(--accent); flex-shrink: 0;
}
.panel-title {
  font-family: 'Lora', serif; font-size: 1.05rem; font-weight: 700;
  color: var(--accent); letter-spacing: 0.02em;
  display: flex; align-items: center; gap: 8px;
}
.panel textarea {
  flex: 1; border: none; outline: none; background: var(--surface2);
  padding: 12px 16px; font-family: 'Courier New', monospace;
  font-size: 0.92rem; line-height: 1.6; color: var(--text); resize: none; overflow-y: auto;
}
/* Variante verde */
.panel.panel-green { border-color: var(--green); }
.panel.panel-green .panel-header { background: var(--green-light); border-bottom-color: var(--green); }
.panel.panel-green .panel-title { color: var(--green); }

@media (max-width: 600px) {
  .panels-grid { grid-template-columns: 1fr; flex: none; }
  .panel textarea { min-height: 200px; }
}
```

### Panels dos columnas — glass (Sistema B Premium)

```css
.panel {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: var(--radius); box-shadow: var(--shadow);
  display: flex; flex-direction: column; overflow: hidden;
  transition: box-shadow 0.3s, transform 0.3s;
}
.panel:hover { box-shadow: var(--shadow-hover); transform: translateY(-2px); }
.panel-header {
  display: flex; align-items: center; justify-content: space-between;
  padding: 10px 16px; flex-shrink: 0;
  backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px);
  background: rgba(26,58,92,0.06); border-bottom: 1px solid var(--border);
}
.panel-title {
  font-family: 'Lora', serif; font-size: 1.05rem; font-weight: 700;
  color: var(--accent); letter-spacing: 0.02em;
  display: flex; align-items: center; gap: 8px;
}
/* Iconos SVG inline en .panel-title en vez de emojis */
.panel-title svg { width: 18px; height: 18px; stroke: currentColor; fill: none; stroke-width: 2; }
.panel textarea {
  flex: 1; border: none; outline: none; background: var(--surface2);
  padding: 12px 16px;
  font-family: 'SF Mono', 'JetBrains Mono', 'Fira Code', 'Consolas', monospace;
  font-size: 0.88rem; line-height: 1.6; color: var(--text); resize: none; overflow-y: auto;
}
/* Custom scrollbar */
.panel textarea::-webkit-scrollbar { width: 6px; }
.panel textarea::-webkit-scrollbar-track { background: transparent; }
.panel textarea::-webkit-scrollbar-thumb {
  background: var(--accent-light); border-radius: 3px;
}
/* Variante verde */
.panel.panel-green { border-color: rgba(22,163,74,0.2); }
.panel.panel-green .panel-header {
  background: rgba(22,163,74,0.06); border-bottom-color: rgba(22,163,74,0.15);
}
.panel.panel-green .panel-title { color: var(--green); }
```

### Tooltip copiar (Sistema B)

```css
.copy-wrap { position: relative; }
.copy-tooltip {
  position: absolute; background: var(--accent); color: white;
  padding: 3px 12px; border-radius: 6px; font-size: 0.72rem; font-weight: 600;
  top: -32px; left: 50%; transform: translateX(-50%) translateY(4px);
  white-space: nowrap; opacity: 0; pointer-events: none;
  transition: opacity 0.3s, transform 0.3s;
}
.copy-tooltip.show { opacity: 1; transform: translateX(-50%) translateY(0); }
```

### Category pills (Sistema B Premium)

```css
.cat-nav {
  margin-bottom: 10px;
  animation: fadeInUp 0.6s ease-out 0.05s both;
}
.cat-pills {
  display: flex; gap: 8px; overflow-x: auto;
  padding: 4px 0; -webkit-overflow-scrolling: touch;
  scrollbar-width: none;
}
.cat-pills::-webkit-scrollbar { display: none; }
.cat-pill {
  flex-shrink: 0; padding: 8px 16px;
  border-radius: 999px; border: 1.5px solid var(--border);
  background: var(--surface); color: var(--text-muted);
  font-family: 'Inter', sans-serif; font-size: 12px; font-weight: 600;
  cursor: pointer; transition: all 0.2s;
  display: flex; align-items: center; gap: 6px;
}
.cat-pill:hover { border-color: var(--accent); color: var(--accent); }
.cat-pill.active {
  background: var(--accent); color: white;
  border-color: var(--accent); box-shadow: 0 2px 8px rgba(26,58,92,0.25);
}
.cat-pill .count {
  font-size: 10px; opacity: 0.7;
  background: rgba(255,255,255,0.2); padding: 1px 6px; border-radius: 999px;
}
```

### Boton copiar con icono SVG (Sistema B Premium)

```css
.btn-copy {
  display: inline-flex; align-items: center; gap: 6px;
  padding: 6px 14px; border-radius: 8px;
  font-size: 12px; font-weight: 600;
  font-family: 'Inter', sans-serif;
  cursor: pointer; transition: all 0.2s; border-width: 1.5px; border-style: solid;
  background: transparent;
}
.btn-copy svg { width: 14px; height: 14px; stroke: currentColor; fill: none; stroke-width: 2; }
.btn-copy.blue { color: var(--accent); border-color: var(--accent); }
.btn-copy.blue:hover { background: var(--accent); color: white; }
.btn-copy.green { color: var(--green); border-color: var(--green); }
.btn-copy.green:hover { background: var(--green); color: white; }
```

### Header premium con degradado (Sistema B Premium)

```css
.app-header {
  background: linear-gradient(135deg, #0f2240 0%, #1a3a5c 50%, #234e77 100%);
  color: white; padding: 40px 32px 32px;
  border-radius: var(--radius-lg); position: relative; overflow: hidden;
  margin-bottom: 6px; box-shadow: 0 8px 32px rgba(15,34,64,0.25);
  animation: fadeInUp 0.6s ease-out;
}
.app-header::before {
  content: ''; position: absolute; top: -80px; right: -30px;
  width: 250px; height: 250px; border-radius: 50%;
  background: radial-gradient(circle, rgba(14,165,233,0.12) 0%, transparent 70%);
  filter: blur(40px);
}
.app-header::after {
  content: ''; position: absolute; bottom: -60px; left: 15%;
  width: 200px; height: 200px; border-radius: 50%;
  background: radial-gradient(circle, rgba(139,92,246,0.08) 0%, transparent 70%);
  filter: blur(40px);
}
.app-header h1 {
  font-family: 'Lora', serif; color: white;
  font-size: clamp(1.3rem, 3vw, 1.7rem); font-weight: 700;
}
.app-header .subtitle { font-size: 13px; color: rgba(255,255,255,0.6); margin-top: 4px; }

/* Dark mode override */
[data-theme="dark"] .app-header {
  background: linear-gradient(135deg, #0a1628 0%, #111827 50%, #1a2540 100%);
  box-shadow: 0 8px 32px rgba(0,0,0,0.4);
}
```

### Animaciones (Sistema B Premium)

```css
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(16px); }
  to { opacity: 1; transform: translateY(0); }
}
@keyframes textFlash {
  0% { background-color: var(--accent-light); }
  100% { background-color: var(--surface2); }
}
/* Uso escalonado */
.app-header { animation: fadeInUp 0.6s ease-out; }
.card       { animation: fadeInUp 0.6s ease-out 0.1s both; }
.panels-grid { animation: fadeInUp 0.6s ease-out 0.2s both; }
.panel textarea.flash { animation: textFlash 0.4s ease-out; }
```

---

## 6. Patrones JavaScript

### Vanilla JS obligatorio

Sin jQuery, sin React, sin build tools. Todo en un `<script>` al final del body.

### Toast

```javascript
function mostrarToast(msg) {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.classList.add('show');
  clearTimeout(t._timer);
  t._timer = setTimeout(() => t.classList.remove('show'), 2200);
}
```

### Clipboard (API moderna — preferida)

```javascript
function copiarTexto(id) {
  const text = document.getElementById(id).value;
  navigator.clipboard.writeText(text).then(() => {
    const label = id === 'tratamientoAlta' ? 'Tratamiento' : 'Hoja Operatoria';
    mostrarToast('✓  ' + label + ' copiado');
  });
}
```

> **Nota:** Usar siempre `navigator.clipboard.writeText()` (API moderna). No usar `document.execCommand('copy')` (deprecated).

### localStorage con expiracion diaria

```javascript
// Guardar
localStorage.setItem('clave', valor);
localStorage.setItem('clave-date', new Date().toDateString());

// Leer (solo si es de hoy)
const saved = localStorage.getItem('clave');
const savedDate = localStorage.getItem('clave-date');
if (saved && savedDate === new Date().toDateString()) {
  // usar saved
} else {
  localStorage.removeItem('clave');
  localStorage.removeItem('clave-date');
}
```

### Busqueda con normalizacion Unicode

```javascript
function normalizar(str) {
  return str.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
}
```

### Fecha actual

```javascript
function hoy() {
  const d = new Date();
  const dd = String(d.getDate()).padStart(2, '0');
  const mm = String(d.getMonth() + 1).padStart(2, '0');
  const yy = String(d.getFullYear()).slice(-2);
  return `${dd}/${mm}/${yy}`;
}
```

### Formato moneda

```javascript
const fmt = n => n.toLocaleString('es-ES', {
  minimumFractionDigits: 2, maximumFractionDigits: 2
}) + ' €';
```

### Event handling

- **Acciones simples:** `onclick="funcion()"` inline
- **Logica compleja:** `element.addEventListener('input', handler)`
- **Inicializacion:** `DOMContentLoaded` o script al final del body

### Organizacion del codigo

```javascript
// ─────────────────────────────────────────────
//  NOMBRE DE SECCION
// ─────────────────────────────────────────────
```

---

## 7. Diseno responsive

### Breakpoints

| Breakpoint | Uso |
|-----------|-----|
| `@media (max-width: 600px)` | **Primario** — grids a 1 col, forms apilados, back-button reducido |
| `@media (max-width: 768px)` | Secundario — grids 2 col a 1 col |
| `@media (max-width: 480px)` | Terciario — logos/iconos grid reduction |

### Ajustes movil comunes

```css
@media (max-width: 600px) {
  /* Si el contenedor usa 100vh */
  html, body { height: auto; overflow: auto; }
  #app { height: auto; padding-bottom: 20px; }

  /* Forms */
  .form-row { flex-direction: column; }
  .form-group { width: 100%; }

  /* Grids */
  .panels-grid { grid-template-columns: 1fr; }
  .grid { grid-template-columns: 1fr; }

  /* Back button */
  .back-home { padding: 4px 8px; font-size: 10px; }

  /* B Premium: header y pills */
  .app-header { padding: 32px 20px 24px; border-radius: var(--radius); }
  .app-header::before, .app-header::after { display: none; } /* ocultar glows */
  .theme-toggle { width: 36px; height: 36px; font-size: 1.1rem; }
  .cat-pills { gap: 6px; } /* scroll horizontal natural */
}
```

### Tipografia fluid

```css
font-size: clamp(2rem, 5vw, 3.2rem);   /* Sistema A h1 */
font-size: clamp(1.3rem, 3vw, 1.7rem); /* Sistema B h1 */
```

---

## 8. Modo oscuro (opcional, solo Sistema B)

### CSS — override de variables

```css
[data-theme="dark"] {
  --bg: #111827;
  --surface: #1f2937;
  --surface2: #283244;
  --border: #374151;
  --border-light: #4b5563;
  --text: #f1f5f9;
  --text-muted: #a8b8cc;
  --text-light: #64748b;
  --accent: #93c5fd;
  --accent-hover: #bae0ff;
  --accent-light: #1e3a5f;
  --green-light: #14352a;
  --amber-light: #3b2a10;
  --red-light: #3b1010;
  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.15);
  --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.2);
  --shadow-hover: 0 20px 25px -5px rgb(0 0 0 / 0.3);
}
```

### HTML — boton toggle

```html
<button class="theme-toggle" id="btn-theme" title="Cambiar tema"></button>
```

```css
.theme-toggle {
  position: absolute; top: 0.3rem; right: 0.3rem;
  background: var(--surface2); border: 1.5px solid var(--border);
  border-radius: 50%; width: 42px; height: 42px; font-size: 1.3rem;
  cursor: pointer; display: flex; align-items: center; justify-content: center;
  box-shadow: var(--shadow); transition: border-color 0.2s, box-shadow 0.2s;
}
.theme-toggle:hover { border-color: var(--accent); box-shadow: var(--shadow-hover); }
```

### JS — auto-deteccion + toggle manual

```javascript
const btnTheme = document.getElementById('btn-theme');

function applyTheme(dark) {
  if (dark) {
    document.documentElement.setAttribute('data-theme', 'dark');
    btnTheme.textContent = '☀️';
  } else {
    document.documentElement.removeAttribute('data-theme');
    btnTheme.textContent = '🌙';
  }
}

function getAutoTheme() {
  const hour = new Date().getHours();
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  return (hour >= 21 || hour < 7 || prefersDark) ? 'dark' : 'light';
}

function initTheme() {
  const saved = localStorage.getItem('theme');
  const savedDate = localStorage.getItem('theme-date');
  const today = new Date().toDateString();
  if (saved && savedDate === today) {
    applyTheme(saved === 'dark');
  } else {
    localStorage.removeItem('theme');
    localStorage.removeItem('theme-date');
    applyTheme(getAutoTheme() === 'dark');
  }
}

btnTheme.addEventListener('click', () => {
  const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
  applyTheme(!isDark);
  localStorage.setItem('theme', isDark ? 'light' : 'dark');
  localStorage.setItem('theme-date', new Date().toDateString());
});

window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
  const saved = localStorage.getItem('theme');
  const savedDate = localStorage.getItem('theme-date');
  if (!saved || savedDate !== new Date().toDateString()) {
    applyTheme(getAutoTheme() === 'dark');
  }
});

initTheme();
```

---

## 9. Checklist de despliegue

### Estructura del repositorio

```
{repo-name}/
├── index.html          # App completa (single file)
├── icon.png / icon.svg # Icono de la app
├── .gitignore
├── LICENSE             # MIT
└── README.md
```

### .gitignore estandar

```
.DS_Store
Thumbs.db
Desktop.ini
*.swp
*.swo
*~
.vscode/
.idea/
*.log
```

### README.md template

```markdown
# {Emoji} {Nombre}

{Descripcion en una linea}

## Acceso directo
[Abrir la aplicacion](https://jmacot.github.io/{repo-name}/)

## Funcionalidades
- ...

## Tecnologia
- HTML5, CSS3 y JavaScript puro
- Tipografias: {fuentes} (Google Fonts)
- Sin frameworks, sin dependencias

## Licencia
MIT
```

### GitHub Pages

- Source: branch `main`, root `/`
- Topics: `orthopedic-surgery`, `clinical-tool`, `single-file-html`, `github-pages`

### PWA meta tags (obligatorios en Sistema B)

```html
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="{NOMBRE_CORTO}">
<meta name="theme-color" content="#1a3a5c">
```

### Al publicar una nueva herramienta

1. Crear repo con la estructura anterior
2. Activar GitHub Pages
3. Anadir topics
4. **Actualizar landing page** `jmacot.github.io/index.html` con nueva card
5. Anadir entrada en `.claude/launch.json` para dev server local
