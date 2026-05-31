# Fase 4 - Integración y pruebas End-to-End

## Objetivo

Verifica que la API Flask y el Dashboard Dash funcionen juntos. El sistema debe reflejar automáticamente en el Dashboard los cambios realizados mediante la API, sin recargar manualmente la página.

## Paso 1: iniciar la API en segundo plano

### Windows PowerShell

```powershell
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PWD'; .\venv\Scripts\Activate.ps1; python API.py"
```

### Unix, Linux o macOS

```bash
source venv/bin/activate
python API.py &
```

Verifica:

```bash
curl http://127.0.0.1:5000/sensores
```

Registra el resultado en `BITACORA.md`.

## Paso 2: iniciar el Dashboard en segundo plano

### Windows PowerShell

```powershell
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PWD'; .\venv\Scripts\Activate.ps1; python Dashboard.py"
```

### Unix, Linux o macOS

```bash
source venv/bin/activate
python Dashboard.py &
```

Abre:

```text
http://127.0.0.1:8050
```

## Paso 3: confirmar servicios activos

Ejecuta:

### API

```bash
curl http://127.0.0.1:5000/sensores
```

### Dashboard

Abre en navegador:

```text
http://127.0.0.1:8050
```

Confirma que ambos servicios están activos al mismo tiempo.

## Paso 4: realizar POST a la API

Ejecuta un POST para agregar un nuevo sensor.

### Windows PowerShell

```powershell
curl.exe -X POST http://127.0.0.1:5000/sensores -H "Content-Type: application/json" -d "{\"nombre\":\"Sensor Corriente 1\",\"tipo\":\"corriente\",\"valor\":4.8,\"unidad\":\"A\",\"ubicacion\":\"Tablero electrico\"}"
```

### Unix, Linux o macOS

```bash
curl -X POST http://127.0.0.1:5000/sensores \
  -H "Content-Type: application/json" \
  -d '{"nombre":"Sensor Corriente 1","tipo":"corriente","valor":4.8,"unidad":"A","ubicacion":"Tablero electrico"}'
```

## Paso 5: verificar actualización automática

Observa el Dashboard durante al menos 5 segundos.

Debes confirmar:

1. El nuevo sensor aparece sin recargar la página.
2. Los dropdowns incluyen el nuevo tipo o ubicación si corresponde.
3. El gráfico se actualiza.
4. Las tarjetas de mínimo, máximo y promedio se recalculan.

Si el Dashboard no se actualiza:

1. Verifica que `dcc.Interval` esté configurado en `2000`.
2. Verifica que el callback vuelva a consultar la API.
3. Revisa la consola de Dash.
4. Corrige `Dashboard.py`.
5. Registra el problema y la solución en `BITACORA.md`.

## Paso 6: guardar capturas

Guarda evidencia en:

```text
capturas/
```

Nombres sugeridos:

```text
capturas/fase_4_api_dashboard_activos.png
capturas/fase_4_post_api.png
capturas/fase_4_dashboard_actualizado.png
```

## Paso 7: actualizar bitácora

Registra:

```markdown
## Fase 4 completada
- Hora:
- API ejecutada en segundo plano:
- Dashboard ejecutado en segundo plano:
- POST realizado:
- Sensor agregado:
- Dashboard actualizado sin recargar:
- Capturas guardadas:
- Observaciones:
```

## Criterio de aceptación

La Fase 4 queda aprobada si:

1. API y Dashboard funcionan simultáneamente.
2. Un POST a la API agrega datos correctamente.
3. El Dashboard muestra el cambio sin recargar la página.
4. Las tarjetas y el gráfico se actualizan.
5. La evidencia está guardada en `capturas/`.
6. `BITACORA.md` está actualizado.
