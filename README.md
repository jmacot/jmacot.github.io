<div align="center">

# 🏥 Herramientas COT — redirección

**Este dominio ya no aloja las herramientas clínicas: solo redirige a la app.**

[![Destino](https://img.shields.io/badge/ir_a-app.jmacot.com-38bdf8?style=for-the-badge&logo=cloudflare&logoColor=white)](https://app.jmacot.com)
[![Licencia](https://img.shields.io/badge/licencia-All_Rights_Reserved-red?style=for-the-badge)]()

</div>

---

## Qué es este repo hoy

Una única página que dice «nos hemos mudado» y lleva a **[app.jmacot.com](https://app.jmacot.com)**, con `<meta refresh>` a los 4 segundos y un botón por si el navegador no redirige solo.

Desde **mayo de 2026** las herramientas clínicas se sirven desde una app privada en Cloudflare Pages, detrás de login y con aprobación manual de cada cuenta. Antes de eso, este portal las listaba y las protegía con una contraseña compartida (StatiCrypt); ese modelo se retiró: la contraseña única no distinguía entre usuarios y no permitía revocar accesos.

Los repositorios de las herramientas pasaron a **privados** al mudarse. Los enlaces del tipo `jmacot.github.io/<herramienta>` **ya no responden**.

---

## Lo que sí sigue vivo en este dominio

Son repos independientes, públicos y sin login:

| Sitio | Qué es |
|-------|--------|
| **[/ilustracot](https://jmacot.github.io/ilustracot/)** | Generador de prompts para ilustraciones médicas de COT |
| **[/pacientes](https://jmacot.github.io/pacientes/)** | Guías de rehabilitación y cuidados postoperatorios, escritas para pacientes |

---

## Estructura

```
index.html               ← la página de redirección (esto es todo lo que se sirve)
icon.svg                 ← icono
password_template.html   ← restos del portal StatiCrypt anterior, ya sin uso
password_preview.html    ←   ídem
tools/                   ←   ídem
LICENSE · _config.yml
```

---

## Licencia

All Rights Reserved — ver [LICENSE](LICENSE).
