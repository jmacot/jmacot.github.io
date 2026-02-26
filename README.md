<div align="center">

# 🏥 Herramientas de Cirugía Ortopédica y Traumatología

**Portal web con herramientas clínicas y administrativas para el día a día en COT**

[![Sitio web](https://img.shields.io/badge/web-jmacot.github.io-1a3a5c?style=for-the-badge&logo=github&logoColor=white)](https://jmacot.github.io)
[![Aplicaciones](https://img.shields.io/badge/apps-7-16a34a?style=for-the-badge)]()
[![Licencia](https://img.shields.io/badge/licencia-MIT-blue?style=for-the-badge)]()

---

*Aplicaciones web estáticas, sin instalación, sin dependencias —*
*se abren en cualquier navegador.*

</div>

---

## Aplicaciones

### 📋 Quirófano

| App | Descripción | Enlace |
|-----|-------------|--------|
| **Plantillas Quirúrgicas COT** | 78 plantillas de notas operatorias y tratamientos al alta en 5 regiones anatómicas. Diseño premium con modo oscuro. | [Abrir app](https://jmacot.github.io/plantillas-qx) \| [Repo](https://github.com/jmacot/plantillas-qx) |

### 🦴 Planificación

| App | Descripción | Enlace |
|-----|-------------|--------|
| **CPAK Planner** | Clasificación CPAK y planificación de alineación coronal en artroplastia total de rodilla. Calcula aHKA, JLO, JLCA y fenotipo. | [Abrir app](https://jmacot.github.io/CPAK) \| [Repo](https://github.com/jmacot/CPAK) |
| **Analizador de Planning** | Analiza el planning mensual del servicio de COT. Dashboard D3.js, comparador interactivo, radar, rankings y exportación PDF/ICS. | [Abrir app](https://jmacot.github.io/planning-cot) \| [Repo](https://github.com/jmacot/planning-cot) |

### 📝 Documentación

| App | Descripción | Enlace |
|-----|-------------|--------|
| **Consentimientos Informados** | +210 consentimientos informados de SECOT y SAS organizados por patología con buscador en tiempo real. | [Abrir app](https://jmacot.github.io/consentimientos) \| [Repo](https://github.com/jmacot/consentimientos) |
| **Solicitud de Material Externo** | Formulario para solicitar material quirúrgico externo. 8 proveedores, catálogo de 30+ materiales y generación de PDF. | [Abrir app](https://jmacot.github.io/Material-Externo) \| [Repo](https://github.com/jmacot/Material-Externo) |

### 💰 Administración

| App | Descripción | Enlace |
|-----|-------------|--------|
| **Calculadora de Guardias** | Calcula retribución bruta, neta e IRPF de guardias médicas. 5 configuraciones: HSJD, Vithas, SAS y combinadas. Layout 2 columnas en desktop. | [Abrir app](https://jmacot.github.io/calculadora-guardias) \| [Repo](https://github.com/jmacot/calculadora-guardias) |
| **Analizador de Nómina** | Analiza nóminas del SAS en PDF. Desglose de devengos, deducciones y empresa. Multi-nómina con gráficos de evolución. | [Abrir app](https://jmacot.github.io/nominas-cot) \| [Repo](https://github.com/jmacot/nominas-cot) |

---

## Tecnología

```
HTML5 + CSS3 + JavaScript vanilla
```

- **Zero dependencias** — cada app es un archivo HTML autocontenido.
- **GitHub Pages** — desplegadas directamente desde el repositorio.
- **Responsive** — adaptadas a móvil, tablet y escritorio.
- **Modo oscuro** — landing page y todas las apps con detección automática y toggle manual.
- **Offline-ready** — funcionan sin conexión tras la primera carga.

---

## Inicio rápido

1. Visita **[jmacot.github.io](https://jmacot.github.io)** y elige una herramienta.
2. O clona cualquier repositorio individual y abre el `index.html` en tu navegador.

```bash
git clone https://github.com/jmacot/plantillas-qx.git
open plantillas-qx/index.html
```

---

## Estructura

```
jmacot.github.io/          ← este repo (portal principal)
├── index.html              ← landing page con filtros por categoría
├── LICENSE
├── .gitignore
└── README.md

Cada herramienta vive en su propio repositorio:
├── calculadora-guardias/
├── consentimientos/
├── CPAK/
├── Material-Externo/
├── nominas-cot/
├── planning-cot/
└── plantillas-qx/
```

---

## Licencia

MIT — consulta el archivo [LICENSE](LICENSE) para más detalles.

---

<div align="center">

**[jmacot.github.io](https://jmacot.github.io)** · Herramientas de uso clínico

</div>
