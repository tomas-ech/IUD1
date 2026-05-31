# Fase 2 - Desarrollo de la API REST en Flask

## Objetivo

Crea el backend del proyecto usando Flask. La API debe gestionar datos simulados de sensores almacenados en `sensores.json`.

No avances a la Fase 3 hasta probar todos los endpoints con `curl` y registrar evidencia en `BITACORA.md`.

## Paso 1: crear datos simulados

Crea el archivo `sensores.json` en la raíz del proyecto con una estructura similar:

```json
[
  {
    "id": 1,
    "nombre": "Sensor Temperatura 1",
    "tipo": "temperatura",
    "valor": 24.5,
    "unidad": "C",
    "ubicacion": "Laboratorio"
  },
  {
    "id": 2,
    "nombre": "Sensor Humedad 1",
    "tipo": "humedad",
    "valor": 58.2,
    "unidad": "%",
    "ubicacion": "Laboratorio"
  },
  {
    "id": 3,
    "nombre": "Sensor Presion 1",
    "tipo": "presion",
    "valor": 101.3,
    "unidad": "kPa",
    "ubicacion": "Banco de pruebas"
  }
]
```

Registra la creación del archivo en `BITACORA.md`.

## Paso 2: crear `API.py`

Crea el archivo `API.py` con una API Flask que implemente los siguientes endpoints:

| Método | Ruta | Función |
|---|---|---|
| GET | `/sensores` | Listar todos los sensores |
| GET | `/sensores/<id>` | Obtener un sensor por ID |
| POST | `/sensores` | Crear un nuevo sensor |
| PUT | `/sensores/<id>` | Actualizar un sensor existente |
| DELETE | `/sensores/<id>` | Eliminar un sensor |

## Requisitos de validación

La API debe validar que cada sensor tenga:

| Campo | Tipo esperado | Obligatorio |
|---|---|---|
| `nombre` | texto | Sí |
| `tipo` | texto | Sí |
| `valor` | número | Sí |
| `unidad` | texto | Sí |
| `ubicacion` | texto | Sí |

Instrucciones obligatorias:

1. Si falta un campo obligatorio, responde con código `400`.
2. Si `valor` no es numérico, responde con código `400`.
3. Si se consulta un ID inexistente, responde con código `404`.
4. Después de POST, PUT o DELETE, actualiza `sensores.json`.
5. Usa respuestas JSON en todos los endpoints.

## Paso 3: ejecutar la API

Con el entorno virtual activo, ejecuta:

### Windows PowerShell

```powershell
python API.py
```

### Unix, Linux o macOS

```bash
python API.py
```

La API debe quedar disponible en:

```text
http://127.0.0.1:5000
```

## Paso 4: probar endpoints con curl

Ejecuta las pruebas desde otra terminal.

### GET general

```bash
curl http://127.0.0.1:5000/sensores
```

### GET por ID

```bash
curl http://127.0.0.1:5000/sensores/1
```

### POST

#### Windows PowerShell

```powershell
curl.exe -X POST http://127.0.0.1:5000/sensores -H "Content-Type: application/json" -d "{\"nombre\":\"Sensor Vibracion 1\",\"tipo\":\"vibracion\",\"valor\":12.7,\"unidad\":\"mm/s\",\"ubicacion\":\"Motor principal\"}"
```

#### Unix, Linux o macOS

```bash
curl -X POST http://127.0.0.1:5000/sensores \
  -H "Content-Type: application/json" \
  -d '{"nombre":"Sensor Vibracion 1","tipo":"vibracion","valor":12.7,"unidad":"mm/s","ubicacion":"Motor principal"}'
```

### PUT

#### Windows PowerShell

```powershell
curl.exe -X PUT http://127.0.0.1:5000/sensores/1 -H "Content-Type: application/json" -d "{\"nombre\":\"Sensor Temperatura Actualizado\",\"tipo\":\"temperatura\",\"valor\":26.4,\"unidad\":\"C\",\"ubicacion\":\"Laboratorio\"}"
```

#### Unix, Linux o macOS

```bash
curl -X PUT http://127.0.0.1:5000/sensores/1 \
  -H "Content-Type: application/json" \
  -d '{"nombre":"Sensor Temperatura Actualizado","tipo":"temperatura","valor":26.4,"unidad":"C","ubicacion":"Laboratorio"}'
```

### DELETE

```bash
curl -X DELETE http://127.0.0.1:5000/sensores/2
```

## Paso 5: guardar evidencia

Toma capturas de:

1. La API ejecutándose en terminal.
2. Resultado del GET general.
3. Resultado del POST.
4. Resultado del PUT o DELETE.

Guarda los archivos en:

```text
capturas/
```

Nombres sugeridos:

```text
capturas/fase_2_api_terminal.png
capturas/fase_2_get_sensores.png
capturas/fase_2_post_sensor.png
capturas/fase_2_put_delete.png
```

## Paso 6: actualizar bitácora

Registra:

```markdown
## Fase 2 completada
- Hora:
- Archivo creado: sensores.json
- Archivo creado: API.py
- Endpoints implementados:
- Comandos curl ejecutados:
- Resultados:
- Capturas guardadas:
- Observaciones:
```

## Criterio de aceptación

La Fase 2 queda aprobada si:

1. `sensores.json` existe y contiene datos válidos.
2. `API.py` ejecuta sin errores.
3. Los 5 endpoints responden correctamente.
4. Las validaciones funcionan.
5. Las capturas están guardadas.
6. `BITACORA.md` está actualizado.
