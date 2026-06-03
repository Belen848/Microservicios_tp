import requests

URL = "http://localhost:8000/pedidos"

def test_redis_caido():

    r = requests.post(
        URL,
        json={
            "producto_id": 1,
            "cantidad": 1
        },
        timeout=5
    )

    data = r.json()

    assert data["status"] == "error"