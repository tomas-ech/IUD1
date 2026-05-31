# EA1 - Desarrollo de un Dashboard básico

## Descripción

Proyecto académico con una API REST en Flask y un Dashboard interactivo en Dash. La API administra datos simulados de sensores y el Dashboard consume esos datos cada 2 segundos para mostrar filtros, tarjetas indicadoras y un gráfico en tiempo real.

## Tecnologías usadas

| Tecnología | Uso |
|---|---|
| Python | Lenguaje principal |
| Flask | API REST |
| Dash | Dashboard web |
| Plotly | Gráfico interactivo |
| Pandas | Procesamiento de datos |
| Requests | Consumo de API desde el Dashboard |

## Estructura del proyecto

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

## Configuración del entorno

### Windows PowerShell

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Unix, Linux o macOS

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Ejecutar la API

Con el entorno virtual activo:

```bash
python API.py
```

URL base:

```text
http://127.0.0.1:5000
```

## Ejecutar el Dashboard

En otra terminal, con el entorno virtual activo:

```bash
python Dashboard.py
```

URL del Dashboard:

```text
http://127.0.0.1:8050
```

## Endpoints de la API

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/sensores` | Lista todos los sensores |
| GET | `/sensores/<id>` | Consulta un sensor por ID |
| POST | `/sensores` | Crea un sensor |
| PUT | `/sensores/<id>` | Actualiza un sensor |
| DELETE | `/sensores/<id>` | Elimina un sensor |

## Ejemplos de prueba

### GET general

```bash
curl http://127.0.0.1:5000/sensores
```

### GET por ID

```bash
curl http://127.0.0.1:5000/sensores/1
```

### POST en Windows PowerShell

```powershell
$body = @{nombre='Sensor Corriente 1'; tipo='corriente'; valor=4.8; unidad='A'; ubicacion='Tablero electrico'} | ConvertTo-Json -Compress
Invoke-RestMethod -Method Post -Uri 'http://127.0.0.1:5000/sensores' -ContentType 'application/json' -Body $body
```

### POST en Unix, Linux o macOS

```bash
curl -X POST http://127.0.0.1:5000/sensores \
  -H "Content-Type: application/json" \
  -d '{"nombre":"Sensor Corriente 1","tipo":"corriente","valor":4.8,"unidad":"A","ubicacion":"Tablero electrico"}'
```

### PUT en Windows PowerShell

```powershell
$body = @{nombre='Sensor Temperatura Actualizado'; tipo='temperatura'; valor=26.4; unidad='C'; ubicacion='Laboratorio'} | ConvertTo-Json -Compress
Invoke-RestMethod -Method Put -Uri 'http://127.0.0.1:5000/sensores/1' -ContentType 'application/json' -Body $body
```

### DELETE

```bash
curl -X DELETE http://127.0.0.1:5000/sensores/2
```

## Dashboard

El Dashboard incluye:

1. Gráfico de líneas con valores de sensores.
2. Dropdown para filtrar por tipo.
3. Dropdown para filtrar por ubicación.
4. Slider para limitar registros visibles.
5. Tarjeta de valor mínimo.
6. Tarjeta de valor máximo.
7. Tarjeta de valor promedio.
8. Actualización automática cada 2 segundos.

## Evidencias

La carpeta `capturas/` está destinada a guardar evidencias visuales de la ejecución. Durante la verificación se confirmó visualmente el Dashboard en el navegador integrado y la actualización automática posterior a un POST.

## Prueba de integración

1. Ejecutar `API.py`.
2. Ejecutar `Dashboard.py`.
3. Abrir `http://127.0.0.1:8050`.
4. Crear un sensor con POST.
5. Esperar al menos 5 segundos.
6. Confirmar que el gráfico y las tarjetas cambian sin recargar la página.
