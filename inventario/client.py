import grpc

import inventario_pb2
import inventario_pb2_grpc


channel = grpc.insecure_channel('localhost:50051')

stub = inventario_pb2_grpc.InventarioServiceStub(channel)

response = stub.ReservarStock(
    inventario_pb2.StockRequest(
        producto_id=1,
        cantidad=2
    )
)

print("Success:", response.success)
print("Mensaje:", response.mensaje)