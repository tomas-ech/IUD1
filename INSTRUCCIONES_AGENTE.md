# INSTRUCCIONES GENERALES PARA EL AGENTE DE IA

## Rol del agente

Actúa como un agente autónomo de desarrollo, documentación y verificación técnica. Tu misión es ayudar a un estudiante de Ingeniería Mecatrónica a construir desde cero, probar y documentar el proyecto académico:

**EA1 - Desarrollo de un Dashboard básico**

Debes trabajar como si fueras responsable de entregar un proyecto funcional, ordenado y verificable. No expliques de forma pedagógica innecesaria; ejecuta, verifica, documenta y deja evidencia.

## Objetivo general

Construye una solución compuesta por:

1. Una **API REST en Flask** que gestione datos simulados de sensores.
2. Un **Dashboard interactivo en Dash** que consuma la API.
3. Una integración funcional donde los cambios enviados a la API se reflejen en el Dashboard.
4. Documentación final clara para ejecutar, probar y entregar el proyecto.

## Plan obligatorio de 5 fases

| Fase | Nombre | Resultado esperado |
|---|---|---|
| 1 | Entorno | Python, entorno virtual y dependencias instaladas |
| 2 | API | Backend Flask con endpoints CRUD funcionales |
| 3 | Dashboard | Frontend Dash con actualización automática |
| 4 | Integración | API y Dashboard funcionando juntos |
| 5 | Entrega | README, bitácora, capturas y carpeta limpia |

Debes ejecutar las fases en orden. No avances a una fase nueva sin verificar y documentar la fase anterior.

## Reglas operativas obligatorias

1. Crea y mantén actualizado el archivo `BITACORA.md`.
2. Registra en `BITACORA.md` cada acción importante:
   - Fecha y hora.
   - Comando ejecutado.
   - Archivo creado o modificado.
   - Resultado obtenido.
   - Problemas encontrados y solución aplicada.
3. Crea una carpeta llamada `capturas/`.
4. Guarda capturas de pantalla de los avances principales en `capturas/`.
5. No elimines archivos sin registrar el motivo en la bitácora.
6. No cambies el objetivo del proyecto sin dejar constancia.
7. Verifica cada fase antes de continuar.
8. Usa nombres de archivos exactamente como se indican en estas instrucciones.
9. Documenta comandos para Windows y Unix cuando corresponda.
10. Antes de finalizar, confirma que no queden procesos innecesarios ejecutándose.

## Comandos iniciales sugeridos

### Windows PowerShell

```powershell
New-Item -ItemType Directory -Force capturas
New-Item -ItemType File -Force BITACORA.md
Get-Date | Add-Content BITACORA.md
```

### Unix, Linux o macOS

```bash
mkdir -p capturas
touch BITACORA.md
date >> BITACORA.md
```

## Definition of Done

El proyecto se considera terminado únicamente cuando se cumplan todos estos criterios:

| Criterio | Estado requerido |
|---|---|
| Entorno virtual creado | `venv` existe y puede activarse |
| Dependencias instaladas | `pip list` muestra Flask, Dash, Plotly, Pandas y Requests |
| API creada | Existe `API.py` |
| Datos simulados creados | Existe `sensores.json` |
| Endpoints CRUD | GET, GET por ID, POST, PUT y DELETE funcionan |
| Dashboard creado | Existe `Dashboard.py` |
| Dashboard visible | Abre correctamente en `http://127.0.0.1:8050` |
| Actualización automática | El Dashboard consume la API cada 2 segundos |
| Integración probada | Un POST en la API se refleja en el Dashboard sin recargar |
| Capturas guardadas | La carpeta `capturas/` contiene evidencias |
| Bitácora completa | `BITACORA.md` registra horas, comandos y resultados |
| README final | Existe `README.md` con instrucciones de uso |
| Procesos detenidos | No quedan servidores innecesarios en segundo plano |

Si algún criterio falla, corrige el problema, registra la corrección en `BITACORA.md` y vuelve a verificar.
