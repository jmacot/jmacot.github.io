# Landing Page Redesign — Bento Grid

## Context

The current landing page at `jmacot.github.io` uses a flat grid of equal-sized cards for 8 clinical tools. All cards have identical visual weight, which doesn't reflect actual usage patterns — Plantillas COT is opened daily while CPAK Planner is used rarely. The header is decorative but not functional. Filters and search exist but are overkill for 8 apps. The user (an orthopedic surgeon) opens this page on their phone between surgeries and needs speed over visual showiness.

**Goal:** Replace the flat grid with a Bento Grid layout that creates visual hierarchy, removes unnecessary UI (filters, search, placeholder card), and surfaces key stats in a compact header. The page should feel premium but practical, and scale cleanly to 12+ apps in the future.

**Mockup reference:** `.superpowers/brainstorm/10010-1775253131/content/bento-refined.html`

---

## Design Decisions (validated with user)

| Decision | Choice |
|----------|--------|
| Layout | Bento Grid (option A) |
| Filters + search | Remove both — not needed for 8 apps |
| Placeholder card ("Proximamente") | Remove |
| Category tag pills on cards | Remove — no tags on any card |
| Hero card | Plantillas COT (with arrow CTA) |
| Medium card (beside hero) | Analizador de Planning |
| Arrow indicator | Only on hero card |
| Sky toggle | Keep, positioned top-right of header |
| Dark mode | Keep, same variable overrides as current |

---

## Layout Structure

```
HEADER (compact)
├── Brand: "Suite COT" (gradient) + badge + sky toggle
└── Stats row: 60+ Plantillas | 170+ Consentimientos | 64 Protocolos | 8 Apps

BENTO GRID (3 tiers)
├── Row 1: [Hero: Plantillas COT] [Medium: Analizador de Planning]
├── Row 2: [Small: Rehabilitacion] [Small: Knee Align] [Small: CPAK] [Small: Calc. Guardias]
└── Row 3: [Compact: Material Externo] [Compact: Consentimientos Informados]

FOOTER
└── github.com/jmacot · Herramientas de uso clinico · 2024-2026
```

### Card tier details

| Tier | Cards | Size | Content |
|------|-------|------|---------|
| Hero | Plantillas COT | 1 col, tall | Gradient bg, title, description, stat badge, arrow CTA |
| Medium | Analizador de Planning | 1 col, same row as hero | White/surface bg, title, description, stat badge |
| Small | Rehabilitacion, Knee Align, CPAK Planner, Calc. Guardias | 4-col row | Icon + title + short description, centered |
| Compact | Material Externo, Consentimientos Informados | 2-col row | Icon left + title/description right, horizontal |

### Adding new apps (scalability)

- New app with low usage → add as small card (row 2 becomes 5-col, or overflow to new row)
- New app with high usage → promote to compact or medium tier
- When reaching 12+ apps → consider re-adding search (not filters)
- The grid auto-adjusts: `small-row` uses `repeat(auto-fill, minmax(X, 1fr))` for flexibility

---

## Header

- **Background:** `#0f172a` (same as current), dot grid overlay, 2 glow orbs (sky blue + violet)
- **Brand:** `h1` with "Suite" in white + "COT" in gradient (`linear-gradient(135deg, #38bdf8, #818cf8)`)
- **Badge:** `jmacot.github.io` with green dot, DM Mono 9px, pill shape
- **Sky toggle:** absolute positioned top-right, same implementation as current
- **Stats row:** 4 stats (60+ / 170+ / 64 / 8), DM Serif Display values, DM Mono labels, separated by 1px dividers
- **Dark mode header:** `linear-gradient(135deg, #152238 0%, #1c2f4a 50%, #213656 100%)` per CLAUDE.md

---

## Card Styles

### Shared base (`.cell`)
- `background: var(--surface)`, `border: 1px solid var(--border)`, `border-radius: 16px`
- Hover: `translateY(-3px)` + `var(--shadow-hover)`
- Top accent bar: 3px height with `var(--accent)` color (hero excluded)
- Links (`<a>`) with `text-decoration: none; color: inherit`

### Hero card (`.cell-hero`)
- `background: linear-gradient(135deg, #0c4a6e 0%, #0369a1 50%, #0284c7 100%)`
- White text, radial glow `::after`
- Arrow: 36px circle, `rgba(255,255,255,0.12)`, top-right absolute
- On hover: arrow shifts right 2px, bg brightens
- Dark mode: darker gradient `#0c3553 → #0c4a6e → #075985`
- No top accent bar, no category tag

### Medium card (`.cell-medium`)
- Standard surface bg, larger h2 (1.2rem)
- Flex column, content justified to bottom
- Stat badge in accent color

### Small card (`.cell-small`)
- Centered layout, 38x38px icon with category bg
- h2 at 0.8rem, p at 9px
- No top accent bar
- On mobile: 2-col grid (from 4-col)

### Compact card (`.cell-compact`)
- Horizontal: icon left (36x36), text right
- h2 at 0.82rem, p at 9px
- No top accent bar
- On mobile: 1-col stack

---

## Card Order and URLs

| Position | Tool | URL | Icon color |
|----------|------|-----|-----------|
| Hero | Plantillas COT | `jmacot.github.io/plantillas-qx` | white (on gradient) |
| Medium | Analizador de Planning | `jmacot.github.io/planning-cot` | `--c-administracion` |
| Small 1 | Protocolos y Ejercicios | `jmacot.github.io/rehabilitacion-cot` | `--c-pacientes` |
| Small 2 | Knee Align | `jmacot.github.io/knee-align` | `--c-planificacion` |
| Small 3 | CPAK Planner | `jmacot.github.io/CPAK` | `--c-planificacion` |
| Small 4 | Calculadora de Guardias | `jmacot.github.io/calculadora-guardias` | `--c-administracion` |
| Compact 1 | Material Externo | `jmacot.github.io/Material-Externo` | `--c-documentacion` |
| Compact 2 | Consentimientos Informados | `jmacot.github.io/consentimientos` | `--c-documentacion` |

---

## What Gets Removed

- Filter buttons (`.filters` nav + `filtrar()` JS + `initCounts()`)
- Search input (`.search-wrap` + search event listener + `normalizar()`)
- Placeholder card ("Proximamente")
- Category tag pills (`.card-tag`) from all cards
- Header badge inside header (replaced by inline badge next to brand)
- `header-inner` wrapper (replaced by `header-top` + `header-stats`)
- Old card structure (`.card-meta`, `.card-content`, `.card-icon`, `.card-arrow` on all cards)

## What Gets Kept

- CSS variables (both light and dark)
- Category color system (`--c-quirofano`, etc.)
- Sky toggle (HTML + CSS + JS)
- Dark mode JS (`applyTheme`, `getAutoTheme`, `initTheme`, localStorage)
- Skip link + `#main` target
- `@media (prefers-reduced-motion: reduce)`
- `:focus-visible` styles
- `fadeInUp` animation (staggered per card tier)
- Footer (simplified text)
- Open Graph + meta tags
- Fonts (DM Sans / DM Serif Display / DM Mono)
- Localhost link disable pattern

---

## Responsive (mobile < 600px)

- Header: reduce padding, hide glows, smaller stat text
- Hero card: `grid-column: 1 / -1` (full width), reduced min-height
- Medium card: `grid-column: 1 / -1` (full width)
- Small row: 2 columns (from 4)
- Compact row: 1 column (from 2)
- Sky toggle: `--toggle-size: 18px`

---

## Animations

- Header: `fadeInUp 0.5s ease-out`
- Hero: `fadeInUp 0.5s ease-out 0.05s both`
- Medium: `fadeInUp 0.5s ease-out 0.1s both`
- Small cards: staggered 0.15s → 0.3s
- Compact cards: staggered 0.35s → 0.4s
- All disabled by `prefers-reduced-motion`

---

## Accessibility

- Skip link preserved (`<a href="#main" class="skip-link">`)
- All cards are `<a>` tags (keyboard navigable)
- `:focus-visible` outline on all cells
- Sky toggle: `aria-label="Cambiar modo claro/oscuro"`
- `role` attributes not needed (native `<a>` semantics sufficient)
- Color contrast: all text meets WCAG AA on both themes

---

## Footer

Single line, DM Mono 10px:
```
github.com/jmacot · Herramientas de uso clinico · 2024-2026
```

---

## File Modified

- `/Users/jma/Documents/Proyectos/COT/jmacot.github.io/index.html` — single file, complete rewrite of HTML structure and CSS, JS simplified (remove filter/search, keep theme)

---

## Verification

1. Open `index.html` via local server — verify all 8 cards render in correct positions
2. Click each card — verify correct URL opens
3. Toggle sky toggle — verify dark mode applies correctly to all card tiers
4. Resize to mobile (< 600px) — verify grid collapses: hero full-width, small 2-col, compact 1-col
5. Test on iOS Safari (real device or simulator) — verify touch targets and no overflow
6. Tab through all cards — verify focus-visible outlines
7. Enable reduced-motion in OS — verify no animations
8. Verify hover states on desktop: hero arrow shifts, all cards lift
