syntax = "proto3";

package inventario;

service InventarioService {
  rpc ReservarStock (StockRequest) returns (StockResponse);
}

message StockRequest {
  int32 producto_id = 1;
  int32 cantidad = 2;
}

message StockResponse {
  bool success = 1;
  string mensaje = 2;
}