from fastapi import FastAPI
from pydantic import BaseModel

import grpc
import pika

import inventario_pb2
import inventario_pb2_grpc


app = FastAPI()


class PedidoRequest(BaseModel):
    producto_id: int
    cantidad: int


@app.get("/health")
def health():
    return {"status": "up"}


@app.post("/pedidos")
def crear_pedido(pedido: PedidoRequest):

    # gRPC → Inventario
    channel = grpc.insecure_channel('inventario:50051')

    stub = inventario_pb2_grpc.InventarioServiceStub(channel)

    response = stub.ReservarStock(
        inventario_pb2.StockRequest(
            producto_id=pedido.producto_id,
            cantidad=pedido.cantidad
        )
    )

    if not response.success:
        return {
            "status": "error",
            "mensaje": response.mensaje
        }

    # RabbitMQ → Evento async
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq')
    )

    rabbit_channel = connection.channel()

    rabbit_channel.queue_declare(queue='order_confirmed')

    mensaje = f"Pedido confirmado para producto {pedido.producto_id}"

    rabbit_channel.basic_publish(
        exchange='',
        routing_key='order_confirmed',
        body=mensaje
    )

    connection.close()

    return {
        "status": "ok",
        "mensaje": "Pedido creado correctamente"
    }