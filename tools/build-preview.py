#!/usr/bin/env python3
"""Regenera password_preview.html a partir de password_template.html.

El template tiene placeholders StatiCrypt (`/*[|...|]*/0`) y depende del
motor staticrypt para inicializar. El preview es un mirror del template
con esos placeholders sustituidos por valores fijos y la inicialización
StatiCrypt reemplazada por un stub que muestra el form directamente.

Uso:
    python3 tools/build-preview.py            # regenera el preview
    python3 tools/build-preview.py --check    # falla si está desactualizado

Contraseña de prueba (solo para previsualizar el caso de error):  demo
"""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "password_template.html"
PREVIEW = ROOT / "password_preview.html"

PLACEHOLDERS = {
    "/*[|template_title|]*/0": "Acceso · jmacot.github.io",
    "/*[|template_instructions|]*/0": "Acceso restringido · Introduce la contraseña",
    "/*[|template_error|]*/0": "Contraseña incorrecta",
    "/*[|template_placeholder|]*/0": "Contraseña",
    "/*[|template_toggle_show|]*/0": "Mostrar contraseña",
    "/*[|template_toggle_hide|]*/0": "Ocultar contraseña",
    "/*[|template_remember|]*/0": "Recordarme en este dispositivo",
    "/*[|template_button|]*/0": "Entrar",
}

INIT_STUB = """\
    // PREVIEW: bypass StatiCrypt y muestra form directamente
    window.addEventListener('DOMContentLoaded', function() {
      document.getElementById('staticrypt_loading').classList.add('hidden');
      document.getElementById('staticrypt_content').classList.remove('hidden');
      var pw = document.getElementById('staticrypt-password');
      if (pw) pw.focus();
      requestAnimationFrame(function() { document.body.classList.add('animate'); });
    });

    var templateToggleAltShow = "Mostrar contraseña";
    var templateToggleAltHide = "Ocultar contraseña";
"""

SUBMIT_STUB = """\
      // PREVIEW: simula validación (contraseña correcta = "demo")
      var isSuccessful = (document.getElementById('staticrypt-password').value === 'demo');
      var errorEl = document.getElementById("error-msg");
      if (!isSuccessful) {
        errorEl.classList.add("show");
        var input = document.getElementById("staticrypt-password");
        input.style.borderColor = "#f87171";
        input.style.boxShadow = "0 0 0 4px rgba(248,113,113,.18)";
        setTimeout(function () {
          input.style.borderColor = "";
          input.style.boxShadow = "";
          errorEl.classList.remove("show");
        }, 3000);
      }
    });"""


def build(template: str) -> str:
    src = template
    for k, v in PLACEHOLDERS.items():
        src = src.replace(k, v)

    # Eliminar el bloque "STATICRYPT ENGINE" hasta el cierre de templateConfig
    src = re.sub(
        r"    // ─+\n    //  STATICRYPT ENGINE.*?    \};\n",
        "",
        src,
        count=1,
        flags=re.DOTALL,
    )
    # Reemplazar la inicialización + onload por el stub del preview
    src = re.sub(
        r"    const staticrypt = staticryptInitiator.*?    \};\n",
        INIT_STUB,
        src,
        count=1,
        flags=re.DOTALL,
    )
    # Reemplazar la llamada a handleDecryptionOfPage por validación local
    src = re.sub(
        r"      const \{ isSuccessful \} = await staticrypt\.handleDecryptionOfPage.*?\}\);",
        SUBMIT_STUB,
        src,
        count=1,
        flags=re.DOTALL,
    )
    return src


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="No escribe; sale con código 1 si el preview está desactualizado.",
    )
    args = parser.parse_args()

    template = TEMPLATE.read_text(encoding="utf-8")
    new = build(template)

    if args.check:
        current = PREVIEW.read_text(encoding="utf-8") if PREVIEW.exists() else ""
        if current != new:
            print(
                f"❌ {PREVIEW.name} está desactualizado respecto a {TEMPLATE.name}.\n"
                f"   Ejecuta:  python3 tools/build-preview.py",
                file=sys.stderr,
            )
            return 1
        print(f"✅ {PREVIEW.name} sincronizado con {TEMPLATE.name}")
        return 0

    PREVIEW.write_text(new, encoding="utf-8")
    print(f"✅ {PREVIEW.name} regenerado ({len(new):,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
