"""Descarga las fuentes que no se guardan en el repositorio.

Uso (desde la raíz del repositorio):

    python catalogo/descargar.py              lista las descargas disponibles
    python catalogo/descargar.py ID [ID ...]  descarga las indicadas
    python catalogo/descargar.py --todas      descarga todas

Cada descarga se compara con la suma SHA-256 esperada de catalogo/descargas.csv.
Si la suma no coincide, el archivo se borra y el script avisa.
Si no hay suma esperada, se muestra la calculada para registrarla.
Los archivos descargados están excluidos de Git por .gitignore.
Solo usa la biblioteca estándar de Python.
"""

from __future__ import annotations

import csv
import hashlib
import sys
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
LISTA = RAIZ / "catalogo" / "descargas.csv"
AGENTE = "DatatonPuntoCero-GAMLP/0.1 (catalogo de fuentes; https://github.com/Primero-Los-Datos-de-La-Paz)"


def leer() -> list[dict]:
    with LISTA.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def descargar(fila: dict) -> bool:
    destino = RAIZ / fila["destino"]
    destino.parent.mkdir(parents=True, exist_ok=True)
    print(f"[{fila['id']}] {fila['url']}")
    print(f"  licencia: {fila['licencia']}")
    pedido = urllib.request.Request(fila["url"], headers={"User-Agent": AGENTE})
    suma = hashlib.sha256()
    temporal = destino.with_suffix(destino.suffix + ".parcial")
    with urllib.request.urlopen(pedido, timeout=120) as resp, temporal.open("wb") as fh:
        while bloque := resp.read(1024 * 1024):
            suma.update(bloque)
            fh.write(bloque)
    calculada = suma.hexdigest()
    esperada = fila["sha256_esperado"].strip()
    if esperada and calculada != esperada:
        temporal.unlink()
        print(f"  ERROR: la suma no coincide (esperada {esperada}, obtenida {calculada}). Se borró el archivo.")
        return False
    temporal.replace(destino)
    if esperada:
        print(f"  OK: suma verificada. Guardado en {fila['destino']}")
    else:
        print(f"  Guardado en {fila['destino']}. Suma calculada (regístrala en descargas.csv): {calculada}")
    return True


def main(args: list[str]) -> int:
    filas = leer()
    if not args:
        for f in filas:
            print(f"{f['id']:<26} {f['motivo']}")
        print("\nIndica uno o más ID, o --todas.")
        return 0
    elegidas = filas if args == ["--todas"] else [f for f in filas if f["id"] in args]
    faltan = set(args) - {f["id"] for f in filas} - {"--todas"}
    if faltan:
        print(f"ID desconocidos: {', '.join(sorted(faltan))}")
        return 1
    return 0 if all(descargar(f) for f in elegidas) else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
