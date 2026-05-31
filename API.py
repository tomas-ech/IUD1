from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from flask import Flask, jsonify, request


app = Flask(__name__)
DATA_FILE = Path(__file__).with_name("sensores.json")
REQUIRED_FIELDS = ("nombre", "tipo", "valor", "unidad", "ubicacion")


def load_sensors() -> list[dict[str, Any]]:
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_sensors(sensors: list[dict[str, Any]]) -> None:
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(sensors, file, ensure_ascii=False, indent=2)


def validate_sensor(payload: dict[str, Any]) -> tuple[bool, str | None]:
    for field in REQUIRED_FIELDS:
        if field not in payload:
            return False, f"Falta el campo obligatorio: {field}"
        if field != "valor" and not isinstance(payload[field], str):
            return False, f"El campo {field} debe ser texto"
        if field != "valor" and not payload[field].strip():
            return False, f"El campo {field} no puede estar vacio"

    if not isinstance(payload["valor"], (int, float)):
        return False, "El campo valor debe ser numerico"

    return True, None


def next_id(sensors: list[dict[str, Any]]) -> int:
    if not sensors:
        return 1
    return max(sensor["id"] for sensor in sensors) + 1


@app.get("/sensores")
def get_sensors():
    return jsonify(load_sensors()), 200


@app.get("/sensores/<int:sensor_id>")
def get_sensor(sensor_id: int):
    sensors = load_sensors()
    sensor = next((item for item in sensors if item["id"] == sensor_id), None)
    if sensor is None:
        return jsonify({"error": "Sensor no encontrado"}), 404
    return jsonify(sensor), 200


@app.post("/sensores")
def create_sensor():
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify({"error": "El cuerpo debe ser un objeto JSON"}), 400

    is_valid, error = validate_sensor(payload)
    if not is_valid:
        return jsonify({"error": error}), 400

    sensors = load_sensors()
    sensor = {field: payload[field] for field in REQUIRED_FIELDS}
    sensor["id"] = next_id(sensors)
    sensors.append(sensor)
    save_sensors(sensors)
    return jsonify(sensor), 201


@app.put("/sensores/<int:sensor_id>")
def update_sensor(sensor_id: int):
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify({"error": "El cuerpo debe ser un objeto JSON"}), 400

    is_valid, error = validate_sensor(payload)
    if not is_valid:
        return jsonify({"error": error}), 400

    sensors = load_sensors()
    for index, sensor in enumerate(sensors):
        if sensor["id"] == sensor_id:
            updated = {field: payload[field] for field in REQUIRED_FIELDS}
            updated["id"] = sensor_id
            sensors[index] = updated
            save_sensors(sensors)
            return jsonify(updated), 200

    return jsonify({"error": "Sensor no encontrado"}), 404


@app.delete("/sensores/<int:sensor_id>")
def delete_sensor(sensor_id: int):
    sensors = load_sensors()
    sensor = next((item for item in sensors if item["id"] == sensor_id), None)
    if sensor is None:
        return jsonify({"error": "Sensor no encontrado"}), 404

    sensors = [item for item in sensors if item["id"] != sensor_id]
    save_sensors(sensors)
    return jsonify({"mensaje": "Sensor eliminado", "sensor": sensor}), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
