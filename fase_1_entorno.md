# Fase 1 - Configuración del entorno

## Objetivo

Configura el entorno base de Python para ejecutar la API Flask y el Dashboard Dash.

No avances a la Fase 2 hasta confirmar que el entorno virtual funciona y que las dependencias están instaladas.

## Paso 1: verificar Python

Ejecuta:

### Windows PowerShell

```powershell
python --version
py --version
```

### Unix, Linux o macOS

```bash
python3 --version
python --version
```

Registra en `BITACORA.md` la versión encontrada.

Ejemplo de registro:

```markdown
## Fase 1 - Entorno
- Hora: 2026-05-30 10:00
- Comando: python --version
- Resultado: Python 3.x.x detectado correctamente.
```

## Paso 2: crear el entorno virtual

Ejecuta desde la raíz del proyecto:

### Windows PowerShell

```powershell
python -m venv venv
```

Si `python` no funciona, usa:

```powershell
py -m venv venv
```

### Unix, Linux o macOS

```bash
python3 -m venv venv
```

Verifica que se haya creado la carpeta `venv/`.

## Paso 3: activar el entorno virtual

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la activación, ejecuta:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\Activate.ps1
```

### Windows CMD

```cmd
venv\Scripts\activate.bat
```

### Unix, Linux o macOS

```bash
source venv/bin/activate
```

Confirma que la terminal muestre el prefijo `(venv)`.

## Paso 4: instalar dependencias

Con el entorno virtual activo, ejecuta:

### Windows PowerShell

```powershell
pip install -r requirements.txt
```

### Unix, Linux o macOS

```bash
pip install -r requirements.txt
```

Si `pip` no responde correctamente, usa:

### Windows PowerShell

```powershell
python -m pip install -r requirements.txt
```

### Unix, Linux o macOS

```bash
python3 -m pip install -r requirements.txt
```

## Paso 5: verificar instalación

Ejecuta:

```bash
pip list
```

Confirma que aparezcan estas dependencias:

| Paquete | Requerido |
|---|---|
| Flask | Sí |
| Dash | Sí |
| Plotly | Sí |
| Pandas | Sí |
| Requests | Sí |

## Paso 6: actualizar bitácora

Registra:

```markdown
## Fase 1 completada
- Hora:
- Python verificado:
- Entorno virtual creado:
- Entorno virtual activado:
- Dependencias instaladas:
- Comando de verificación: pip list
- Observaciones:
```

## Criterio de aceptación

La Fase 1 queda aprobada si:

1. Python está instalado.
2. Existe la carpeta `venv/`.
3. El entorno virtual se activa correctamente.
4. `pip list` muestra las dependencias requeridas.
5. `BITACORA.md` contiene el registro de la fase.
