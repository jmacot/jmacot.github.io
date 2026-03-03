<div align="center">

# 🏥 Herramientas de Cirugía Ortopédica y Traumatología

**Portal web con herramientas clínicas y administrativas para el día a día en COT**

[![Sitio web](https://img.shields.io/badge/web-jmacot.github.io-1a3a5c?style=for-the-badge&logo=github&logoColor=white)](https://jmacot.github.io)
[![Aplicaciones](https://img.shields.io/badge/apps-7-16a34a?style=for-the-badge)]()
[![Licencia](https://img.shields.io/badge/licencia-All_Rights_Reserved-red?style=for-the-badge)]()

---

*Aplicaciones web estáticas, sin instalación, sin dependencias —*
*se abren en cualquier navegador.*

</div>

---

## Aplicaciones

### 📋 Quirófano

| App | Descripción | Enlace |
|-----|-------------|--------|
| **Plantillas Quirúrgicas COT** | Más de 60 notas operatorias y tratamientos al alta listos para usar. Elige el procedimiento, personaliza los datos y copia el texto a la historia clínica. | [Abrir app](https://jmacot.github.io/plantillas-qx) \| [Repo](https://github.com/jmacot/plantillas-qx) |

### 🦴 Planificación

| App | Descripción | Enlace |
|-----|-------------|--------|
| **CPAK Planner** | Planifica la alineación coronal en prótesis total de rodilla. Introduce las medidas radiológicas y obtén la clasificación CPAK con el fenotipo del paciente. | [Abrir app](https://jmacot.github.io/CPAK) \| [Repo](https://github.com/jmacot/CPAK) |
| **Analizador de Planning** | Visualiza el planning mensual del servicio. Consulta tu calendario, compara la carga de guardias entre compañeros y revisa la retribución estimada. | [Abrir app](https://jmacot.github.io/planning-cot) \| [Repo](https://github.com/jmacot/planning-cot) |

### 📝 Documentación

| App | Descripción | Enlace |
|-----|-------------|--------|
| **Consentimientos Informados** | Accede a más de 210 consentimientos informados de SECOT y SAS. Busca por patología o navega por categorías para encontrar el documento que necesitas. | [Abrir app](https://jmacot.github.io/consentimientos) \| [Repo](https://github.com/jmacot/consentimientos) |
| **Solicitud de Material Externo** | Solicita material quirúrgico externo en segundos. Elige casa comercial, selecciona el material del catálogo y genera el documento listo para enviar. | [Abrir app](https://jmacot.github.io/Material-Externo) \| [Repo](https://github.com/jmacot/Material-Externo) |

### 💰 Administración

| App | Descripción | Enlace |
|-----|-------------|--------|
| **Calculadora de Guardias** | Calcula lo que vas a cobrar por tus guardias. Selecciona los días en el calendario y consulta el bruto, neto e IRPF para cada centro hospitalario. | [Abrir app](https://jmacot.github.io/calculadora-guardias) \| [Repo](https://github.com/jmacot/calculadora-guardias) |
| **Analizador de Nómina** | Entiende tu nómina mes a mes. Consulta qué significa cada concepto, cuánto has cobrado y cómo evoluciona tu salario. | [Abrir app](https://jmacot.github.io/nominas-cot) \| [Repo](https://github.com/jmacot/nominas-cot) |

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
- **Acceso protegido** — landing page encriptada con StatiCrypt. Sesión de 24 horas compartida con todas las apps.

---

## Acceso

El portal está protegido por contraseña mediante [StatiCrypt](https://github.com/robinmoisson/staticrypt).

1. Visita **[jmacot.github.io](https://jmacot.github.io)** e introduce la clave de acceso.
2. Una vez autenticado, puedes acceder a todas las herramientas sin volver a introducir la contraseña (sesión de 24 horas).
3. Si intentas acceder directamente a una herramienta sin pasar por el portal, serás redirigido automáticamente.

> Para desarrollo local, clona cualquier repositorio y abre el `index.html` en tu navegador.

```bash
git clone https://github.com/jmacot/plantillas-qx.git
open plantillas-qx/index.html
```

---

## Estructura

```
jmacot.github.io/          ← este repo (portal principal)
├── index.html              ← landing page con filtros por categoría
├── password_template.html  ← plantilla de login StatiCrypt
├── .github/workflows/      ← workflow de encriptación y despliegue
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

All Rights Reserved — consulta el archivo [LICENSE](LICENSE) para más detalles.

---

<div align="center">

**[jmacot.github.io](https://jmacot.github.io)** · Herramientas de uso clínico

</div>
