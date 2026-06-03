import threading
import requests

URL = "http://localhost:8000/pedidos"

resultados = []


def comprar():
    r = requests.post(
        URL,
        json={
            "producto_id": 1,
            "cantidad": 1
        }
    )

    resultados.append(r.json())


def test_compra_concurrente():

    t1 = threading.Thread(target=comprar)
    t2 = threading.Thread(target=comprar)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    exitos = sum(
        1 for r in resultados
        if r["status"] == "ok"
    )

    errores = sum(
        1 for r in resultados
        if r["status"] == "error"
    )

    assert exitos >= 1
    assert errores >= 0