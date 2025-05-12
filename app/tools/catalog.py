import csv
from pathlib import Path

CATALOG_PATH = Path("app/data/car_catalog.csv")

def load_catalog():
    with CATALOG_PATH.open(newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        return list(reader)

def search_catalog(make=None, model=None, year=None):
    catalog_data = load_catalog()
    results = []
    for car in catalog_data:
        if make and make.lower() not in car['make'].lower():
            continue
        if model and model.lower() not in car['model'].lower():
            continue
        if year and year != car['year']:
            continue
        results.append(car)
    return results


def search_catalog_tool(make: str = None, model: str = None, year: str = None):
    results = search_catalog(make, model, year)
    if not results:
        return "No se encontraron autos con esos criterios."

    response = "Autos encontrados:\n"
    for auto in results:
        response += f"- {auto['year']} {auto['make']} {auto['model']} {auto['version']} (${auto['price']})\n"
    return response.strip()



tools = [
    {
        "type": "function",
        "function": {
            "name": "search_catalog_tool",
            "description": "Busca autos disponibles en el catálogo.",
            "parameters": {
                "type": "object",
                "properties": {
                    "make": {"type": "string", "description": "Marca del auto (e.g. Volkswagen)"},
                    "model": {"type": "string", "description": "Modelo del auto (e.g. Golf)"},
                    "year": {"type": "string", "description": "Año del auto (e.g. 2020)"},
                },
                "required": []
            }
        }
    }
]