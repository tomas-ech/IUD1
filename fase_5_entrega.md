# Fase 5 - Cierre, documentación y entrega

## Objetivo

Prepara el proyecto para entrega final. Debes generar documentación, revisar evidencias, detener procesos en segundo plano y confirmar que la carpeta está limpia.

## Paso 1: revisar estructura del proyecto

La carpeta final debe contener como mínimo:

```text
.
├── API.py
├── Dashboard.py
├── sensores.json
├── requirements.txt
├── README.md
├── BITACORA.md
├── INSTRUCCIONES_AGENTE.md
├── fase_1_entorno.md
├── fase_2_api.md
├── fase_3_dashboard.md
├── fase_4_integracion.md
├── fase_5_entrega.md
└── capturas/
```

Ejecuta:

### Windows PowerShell

```powershell
Get-ChildItem
Get-ChildItem capturas
```

### Unix, Linux o macOS

```bash
ls -la
ls -la capturas
```

## Paso 2: crear `README.md`

Genera un `README.md` final para el usuario.

Debe incluir:

1. Nombre del proyecto.
2. Descripción breve.
3. Tecnologías usadas.
4. Estructura de archivos.
5. Instrucciones para crear y activar el entorno virtual.
6. Instrucciones para instalar dependencias.
7. Instrucciones para ejecutar `API.py`.
8. Instrucciones para ejecutar `Dashboard.py`.
9. URLs de acceso.
10. Endpoints de la API.
11. Ejemplos de comandos `curl`.
12. Descripción del Dashboard.
13. Evidencias disponibles en `capturas/`.
14. Autor o estudiante, si el dato está disponible.

## Paso 3: revisar `BITACORA.md`

Verifica que `BITACORA.md` incluya:

| Elemento | Requerido |
|---|---|
| Fecha y hora por fase | Sí |
| Comandos ejecutados | Sí |
| Archivos creados | Sí |
| Pruebas realizadas | Sí |
| Errores encontrados | Sí, si existieron |
| Soluciones aplicadas | Sí, si existieron |
| Capturas registradas | Sí |
| Confirmación final | Sí |

Si falta información, actualiza la bitácora antes de entregar.

## Paso 4: verificar capturas

Confirma que exista la carpeta:

```text
capturas/
```

Debe contener evidencias de:

1. Configuración del entorno.
2. API ejecutándose.
3. Pruebas con `curl`.
4. Dashboard abierto.
5. Integración API-Dashboard.
6. Actualización automática después de un POST.

## Paso 5: prueba final de ejecución

Ejecuta una prueba final:

### Terminal 1

```bash
python API.py
```

### Terminal 2

```bash
python Dashboard.py
```

Verifica:

```text
API: http://127.0.0.1:5000/sensores
Dashboard: http://127.0.0.1:8050
```

Registra el resultado final en `BITACORA.md`.

## Paso 6: detener procesos en segundo plano

### Windows PowerShell

Identifica procesos de Python:

```powershell
Get-Process python
```

Detén solo los procesos correspondientes a `API.py` y `Dashboard.py`:

```powershell
Stop-Process -Id <ID_DEL_PROCESO>
```

### Unix, Linux o macOS

Identifica procesos:

```bash
ps aux | grep python
```

Detén solo los procesos correspondientes:

```bash
kill <PID>
```

No detengas procesos ajenos al proyecto.

## Paso 7: limpieza final

Elimina únicamente archivos temporales innecesarios, como:

```text
__pycache__/
.pytest_cache/
```

No elimines:

1. Código fuente.
2. `sensores.json`.
3. `requirements.txt`.
4. `README.md`.
5. `BITACORA.md`.
6. Capturas.
7. Archivos de instrucciones.

## Paso 8: registro final en bitácora

Agrega:

```markdown
## Cierre del proyecto
- Hora:
- README.md generado:
- BITACORA.md revisado:
- Capturas verificadas:
- Prueba final ejecutada:
- Procesos detenidos:
- Carpeta lista para entrega:
- Observaciones finales:
```

## Criterio de aceptación

La Fase 5 queda aprobada si:

1. `README.md` existe y permite ejecutar el proyecto.
2. `BITACORA.md` está completa.
3. Las capturas están organizadas.
4. La prueba final fue realizada.
5. Los procesos en segundo plano fueron detenidos.
6. La carpeta está lista para entrega académica.
