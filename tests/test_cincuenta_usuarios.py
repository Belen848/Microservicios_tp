import threading
import requests

URL = "http://localhost:8000/pedidos"

resultados = []


def comprar():

    r = requests.post(
        URL,
        json={
            "producto_id": 2,
            "cantidad": 1
        }
    )

    resultados.append(r.json())


def test_cincuenta_usuarios():

    threads = []

    for _ in range(50):

        t = threading.Thread(
            target=comprar
        )

        threads.append(t)

        t.start()

    for t in threads:
        t.join()

    exitos = sum(
        1 for r in resultados
        if r["status"] == "ok"
    )

    assert exitos <= 5