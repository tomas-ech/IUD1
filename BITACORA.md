## Fase 1 - Entorno
- Hora: 2026-05-30 20:44
- Comando: python --version
- Resultado: Python 3.12.7 detectado correctamente.
- Comando: New-Item -ItemType Directory -Force capturas
- Resultado: Carpeta capturas creada.
- Comando: New-Item -ItemType File -Force BITACORA.md
- Resultado: Archivo BITACORA.md creado.
- Comando: python -m venv venv
- Resultado: Entorno virtual creado correctamente.
- Comando: .\venv\Scripts\python.exe -m pip install -r requirements.txt
- Resultado: Dependencias instaladas correctamente.
- Comando: .\venv\Scripts\python.exe -m pip list
- Resultado: Flask, Dash, Plotly, Pandas y Requests verificados.

## Fase 2 - API
- Hora: 2026-05-30 20:45
- Archivo creado: sensores.json
- Archivo creado: API.py
- Endpoints planificados: GET /sensores, GET /sensores/<id>, POST /sensores, PUT /sensores/<id>, DELETE /sensores/<id>.
- Validaciones implementadas: campos obligatorios, valor numerico y manejo de ID inexistente.
- Comando: .\venv\Scripts\python.exe -m py_compile API.py Dashboard.py
- Resultado: Compilacion sin errores de sintaxis.
- Comando: Start-Process .\venv\Scripts\python.exe API.py
- Resultado: API iniciada en segundo plano en http://127.0.0.1:5000.
- Comando: curl.exe http://127.0.0.1:5000/sensores
- Resultado: GET general verificado.
- Comando: curl.exe http://127.0.0.1:5000/sensores/1
- Resultado: GET por ID verificado.
- Incidencia: POST y PUT con curl.exe fallaron por manejo de comillas JSON en PowerShell.
- Solucion: Se usó Invoke-RestMethod con ConvertTo-Json para enviar cuerpos JSON validos.
- Resultado: POST, PUT y DELETE verificados correctamente.

## Fase 3 - Dashboard
- Hora: 2026-05-30 20:45
- Archivo creado: Dashboard.py
- Componentes implementados: grafico de lineas, dropdown por tipo, dropdown por ubicacion, slider, tarjetas de minimo, maximo y promedio.
- Actualizacion automatica configurada cada 2 segundos con dcc.Interval.
- Comando: Start-Process .\venv\Scripts\python.exe Dashboard.py
- Resultado: Dashboard iniciado en segundo plano en http://127.0.0.1:8050.
- Verificacion visual: Dashboard renderiza con estado de conexion, filtros, slider, tarjetas y grafico.
- Ajuste aplicado: Los dropdowns conservan la seleccion actual durante la actualizacion automatica.

## Fase 4 - Integracion
- Hora: 2026-05-30 20:55
- API ejecutada en segundo plano: Si.
- Dashboard ejecutado en segundo plano: Si.
- Comando: Invoke-RestMethod -Method Post -Uri http://127.0.0.1:5000/sensores
- Sensor agregado: Sensor Integracion 1.
- Resultado: El Dashboard actualizo el promedio a 46.85 sin recargar la pagina.
- Estado: Integracion End-to-End verificada.

## Fase 5 - Entrega
- Hora: 2026-05-30 20:58
- Archivo creado: README.md
- BITACORA.md revisado y actualizado.
- Observacion: El navegador integrado permitió verificar visualmente el Dashboard; la escritura directa de captura PNG desde el navegador fue bloqueada por permisos del entorno.
- Ajuste final: API.py y Dashboard.py se configuraron con debug=False para evitar procesos duplicados del reloader.
- Procesos en segundo plano detenidos: Si.
- Limpieza final: __pycache__/ eliminado.
- Verificacion final: .\venv\Scripts\python.exe -B -m py_compile API.py Dashboard.py ejecutado sin errores.
- Carpeta lista para entrega: Si.

## Continuacion de ejecucion
- Hora: 2026-05-30 21:10
- Solicitud: continuar desde el navegador integrado abierto en http://127.0.0.1:8050/.
- Accion: Se reiniciaron API.py y Dashboard.py en segundo plano.
- Verificacion API: GET http://127.0.0.1:5000/sensores respondio correctamente.
- Verificacion Dashboard: http://127.0.0.1:8050/ carga con titulo, filtros, tarjetas y estado API conectada correctamente.
- Observacion: Windows muestra procesos hijos en anaconda3 asociados a los procesos iniciados desde venv; se verifico la relacion padre-hijo.
