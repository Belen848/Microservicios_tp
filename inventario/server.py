from concurrent import futures
import grpc
import time

import inventario_pb2
import inventario_pb2_grpc


# Stock fake en memoria
stock_db = {
    1: 10,
    2: 5,
    3: 20
}


class InventarioService(inventario_pb2_grpc.InventarioServiceServicer):

    def ReservarStock(self, request, context):

        producto_id = request.producto_id
        cantidad = request.cantidad

        print(f"Reserva recibida -> Producto {producto_id} | Cantidad {cantidad}")

        if producto_id not in stock_db:
            return inventario_pb2.StockResponse(
                success=False,
                mensaje="Producto no existe"
            )

        if stock_db[producto_id] < cantidad:
            return inventario_pb2.StockResponse(
                success=False,
                mensaje="Stock insuficiente"
            )

        # Reservar stock
        stock_db[producto_id] -= cantidad

        print(f"Stock restante: {stock_db[producto_id]}")

        return inventario_pb2.StockResponse(
            success=True,
            mensaje="Stock reservado correctamente"
        )


def serve():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    inventario_pb2_grpc.add_InventarioServiceServicer_to_server(
        InventarioService(),
        server
    )

    server.add_insecure_port('[::]:50051')

    server.start()

    print("Microservicio Inventario gRPC corriendo en puerto 50051")

    server.wait_for_termination()


if __name__ == '__main__':
    serve()