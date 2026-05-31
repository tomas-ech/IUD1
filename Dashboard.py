from __future__ import annotations

import requests
import pandas as pd
from dash import Dash, Input, Output, State, dcc, html
import plotly.express as px


API_URL = "http://127.0.0.1:5000/sensores"

app = Dash(__name__)
app.title = "EA1 - Dashboard básico"


def fetch_sensors() -> tuple[pd.DataFrame, str]:
    try:
        response = requests.get(API_URL, timeout=3)
        response.raise_for_status()
        data = response.json()
        dataframe = pd.DataFrame(data)
        if dataframe.empty:
            dataframe = pd.DataFrame(columns=["id", "nombre", "tipo", "valor", "unidad", "ubicacion"])
        return dataframe, "API conectada correctamente"
    except requests.RequestException as exc:
        columns = ["id", "nombre", "tipo", "valor", "unidad", "ubicacion"]
        return pd.DataFrame(columns=columns), f"Error de conexión con la API: {exc}"


app.layout = html.Div(
    className="page",
    children=[
        html.H1("EA1 - Desarrollo de un Dashboard básico"),
        html.Div(id="connection-status", className="status"),
        html.Div(
            className="filters",
            children=[
                html.Div(
                    children=[
                        html.Label("Tipo de sensor"),
                        dcc.Dropdown(id="type-filter", clearable=False),
                    ]
                ),
                html.Div(
                    children=[
                        html.Label("Ubicación"),
                        dcc.Dropdown(id="location-filter", clearable=False),
                    ]
                ),
                html.Div(
                    children=[
                        html.Label("Cantidad de registros visibles"),
                        dcc.Slider(
                            id="limit-slider",
                            min=1,
                            max=10,
                            step=1,
                            value=10,
                            marks={1: "1", 5: "5", 10: "10"},
                        ),
                    ]
                ),
            ],
        ),
        html.Div(
            className="cards",
            children=[
                html.Div([html.Span("Mínimo"), html.Strong(id="min-card")], className="card"),
                html.Div([html.Span("Máximo"), html.Strong(id="max-card")], className="card"),
                html.Div([html.Span("Promedio"), html.Strong(id="avg-card")], className="card"),
            ],
        ),
        dcc.Graph(id="sensor-chart"),
        dcc.Interval(id="refresh-interval", interval=2000, n_intervals=0),
    ],
)

app.index_string = """
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #f5f7fb;
                color: #1f2937;
            }
            .page {
                max-width: 1180px;
                margin: 0 auto;
                padding: 28px;
            }
            h1 {
                margin: 0 0 16px;
                font-size: 28px;
            }
            .status {
                margin-bottom: 18px;
                padding: 10px 12px;
                border-left: 4px solid #2563eb;
                background: #ffffff;
            }
            .filters {
                display: grid;
                grid-template-columns: repeat(3, minmax(0, 1fr));
                gap: 16px;
                margin-bottom: 18px;
            }
            label {
                display: block;
                margin-bottom: 6px;
                font-weight: 700;
            }
            .cards {
                display: grid;
                grid-template-columns: repeat(3, minmax(0, 1fr));
                gap: 16px;
                margin-bottom: 18px;
            }
            .card {
                background: white;
                border: 1px solid #e5e7eb;
                border-radius: 8px;
                padding: 16px;
            }
            .card span {
                display: block;
                color: #64748b;
                margin-bottom: 8px;
            }
            .card strong {
                font-size: 26px;
            }
            @media (max-width: 800px) {
                .filters,
                .cards {
                    grid-template-columns: 1fr;
                }
                .page {
                    padding: 18px;
                }
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
"""


@app.callback(
    Output("type-filter", "options"),
    Output("type-filter", "value"),
    Output("location-filter", "options"),
    Output("location-filter", "value"),
    Input("refresh-interval", "n_intervals"),
    State("type-filter", "value"),
    State("location-filter", "value"),
)
def update_filter_options(_n_intervals, current_type, current_location):
    dataframe, _status = fetch_sensors()
    types = sorted(dataframe["tipo"].dropna().unique()) if "tipo" in dataframe else []
    locations = sorted(dataframe["ubicacion"].dropna().unique()) if "ubicacion" in dataframe else []

    type_options = [{"label": "Todos", "value": "todos"}] + [{"label": item, "value": item} for item in types]
    location_options = [{"label": "Todas", "value": "todas"}] + [
        {"label": item, "value": item} for item in locations
    ]
    type_values = {option["value"] for option in type_options}
    location_values = {option["value"] for option in location_options}
    selected_type = current_type if current_type in type_values else "todos"
    selected_location = current_location if current_location in location_values else "todas"
    return type_options, selected_type, location_options, selected_location


@app.callback(
    Output("connection-status", "children"),
    Output("sensor-chart", "figure"),
    Output("min-card", "children"),
    Output("max-card", "children"),
    Output("avg-card", "children"),
    Input("refresh-interval", "n_intervals"),
    Input("type-filter", "value"),
    Input("location-filter", "value"),
    Input("limit-slider", "value"),
)
def update_dashboard(_n_intervals, selected_type, selected_location, limit):
    dataframe, status = fetch_sensors()

    if dataframe.empty:
        figure = px.line(title="No hay datos disponibles")
        return status, figure, "N/A", "N/A", "N/A"

    if selected_type and selected_type != "todos":
        dataframe = dataframe[dataframe["tipo"] == selected_type]
    if selected_location and selected_location != "todas":
        dataframe = dataframe[dataframe["ubicacion"] == selected_location]

    dataframe = dataframe.tail(limit).copy()

    if dataframe.empty:
        figure = px.line(title="No hay datos para los filtros seleccionados")
        return status, figure, "N/A", "N/A", "N/A"

    figure = px.line(
        dataframe,
        x="nombre",
        y="valor",
        color="tipo",
        markers=True,
        title="Valores de sensores en tiempo real",
        labels={"nombre": "Sensor", "valor": "Valor", "tipo": "Tipo"},
    )
    figure.update_layout(margin={"l": 40, "r": 20, "t": 60, "b": 40})

    minimum = dataframe["valor"].min()
    maximum = dataframe["valor"].max()
    average = dataframe["valor"].mean()

    return status, figure, f"{minimum:.2f}", f"{maximum:.2f}", f"{average:.2f}"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8050, debug=False)
