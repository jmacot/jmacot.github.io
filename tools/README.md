# tools/

Utilidades para mantenimiento del repo. No se publican (no las usa GitHub Pages).

## `build-preview.py`

Regenera `password_preview.html` desde `password_template.html`. El preview es
un mirror del template con los placeholders StatiCrypt sustituidos por valores
fijos y la inicialización del motor reemplazada por un stub que muestra el form
directamente (contraseña de prueba: `demo`).

```bash
python3 tools/build-preview.py            # regenera el preview
python3 tools/build-preview.py --check    # falla si está desactualizado
```

Ejecutar **siempre** que se edite `password_template.html`. Los cambios solo
visibles en el preview no llegan al template real y viceversa.
