# Fase 3 - Desarrollo del Dashboard interactivo en Dash

## Objetivo

Crea un Dashboard en Dash que consuma la API Flask y actualice la información automáticamente cada 2 segundos.

No avances a la Fase 4 hasta verificar que el Dashboard renderiza correctamente en `http://127.0.0.1:8050`.

## Paso 1: verificar que la API esté activa

Antes de iniciar el Dashboard, ejecuta la API:

### Windows PowerShell

```powershell
python API.py
```

### Unix, Linux o macOS

```bash
python API.py
```

Verifica:

```bash
curl http://127.0.0.1:5000/sensores
```

Si la API no responde, corrige la Fase 2 antes de continuar.

## Paso 2: crear `Dashboard.py`

Crea el archivo `Dashboard.py` usando Dash.

El Dashboard debe incluir obligatoriamente:

| Componente | Requisito |
|---|---|
| Gráfico de líneas | Mostrar valores de sensores en tiempo real |
| Intervalo automático | Consumir la API cada 2 segundos |
| Dropdown por tipo | Permitir filtrar sensores por tipo |
| Dropdown por ubicación | Permitir filtrar sensores por ubicación |
| Slider | Permitir limitar o ajustar el rango visible de datos |
| Tarjeta 1 | Valor mínimo |
| Tarjeta 2 | Valor máximo |
| Tarjeta 3 | Valor promedio |

## Paso 3: reglas de consumo de API

El Dashboard debe consultar:

```text
http://127.0.0.1:5000/sensores
```

Instrucciones:

1. Usa `requests` para consumir la API.
2. Usa `dcc.Interval` con intervalo de `2000` milisegundos.
3. Convierte la respuesta JSON a un `DataFrame` de Pandas.
4. Si la API no responde, muestra un mensaje de error visible.
5. No detengas el Dashboard si ocurre un error temporal de conexión.
6. Actualiza el gráfico y las tarjetas en cada intervalo.

## Paso 4: diseño mínimo requerido

El Dashboard debe tener:

1. Título del proyecto.
2. Filtros visibles.
3. Tres tarjetas indicadoras.
4. Gráfico principal.
5. Mensaje de estado de conexión con la API.

Los textos deben estar en español.

## Paso 5: ejecutar el Dashboard

Con la API activa en otra terminal, ejecuta:

### Windows PowerShell

```powershell
python Dashboard.py
```

### Unix, Linux o macOS

```bash
python Dashboard.py
```

Abre en el navegador:

```text
http://127.0.0.1:8050
```

## Paso 6: verificar renderizado

Confirma visualmente:

1. El Dashboard carga sin errores.
2. El gráfico de líneas aparece.
3. Las tarjetas muestran mínimo, máximo y promedio.
4. Los dropdowns permiten filtrar.
5. El slider afecta el rango visible.
6. El estado de conexión indica que la API responde.
7. La actualización ocurre cada 2 segundos.

## Paso 7: guardar capturas

Guarda capturas en:

```text
capturas/
```

Nombres sugeridos:

```text
capturas/fase_3_dashboard_general.png
capturas/fase_3_filtros.png
capturas/fase_3_tarjetas.png
capturas/fase_3_grafico.png
```

## Paso 8: actualizar bitácora

Registra:

```markdown
## Fase 3 completada
- Hora:
- Archivo creado: Dashboard.py
- URL probada: http://127.0.0.1:8050
- Componentes verificados:
- Actualización automática verificada:
- Capturas guardadas:
- Observaciones:
```

## Criterio de aceptación

La Fase 3 queda aprobada si:

1. `Dashboard.py` existe.
2. El Dashboard abre en `http://127.0.0.1:8050`.
3. Consume la API Flask.
4. Se actualiza cada 2 segundos.
5. Tiene gráfico, filtros, slider y tres tarjetas.
6. Las capturas están guardadas.
7. `BITACORA.md` está actualizado.
