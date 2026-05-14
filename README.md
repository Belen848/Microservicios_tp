# MPI Microservicios - Sistemas Distribuidos

El objetivo del proyecto es transformar una arquitectura monolítica en una arquitectura basada en microservicios utilizando:

- FastAPI
- gRPC
- RabbitMQ
- Docker
- Docker Compose

---

# Arquitectura

## Microservicios implementados

### MS-02 Pedidos
- API REST pública
- Orquesta el flujo de compra
- Llama a Inventario mediante gRPC
- Publica eventos async en RabbitMQ

### MS-03 Inventario
- Servicio interno gRPC
- Reserva stock
- Evita overselling

### MS-05 Notificaciones
- Consumer RabbitMQ
- Envía notificaciones async

---

# Tecnologías

- Python
- FastAPI
- gRPC
- Protobuf
- RabbitMQ
- Docker

---

# Estructura del proyecto

```bash
Tp-microservicios/

├── inventario/
│ ├── inventario.proto
│ ├── inventario_pb2.py
│ ├── inventario_pb2_grpc.py
│ ├── server.py
│ ├── requirements.txt
│ └── Dockerfile

├── pedidos/
│ ├── main.py
│ ├── inventario_pb2.py
│ ├── inventario_pb2_grpc.py
│ ├── requirements.txt
│ └── Dockerfile

├── notificaciones/
│ ├── worker.py
│ ├── requirements.txt
│ └── Dockerfile

└── docker-compose.yml
```

---

# Requisitos

- Python 3.11+
- Docker Desktop

---

# Instalación

## 1. Clonar repositorio

```bash
git clone URL_DEL_REPO
```

---

## 2. Levantar el sistema

```bash
docker compose up --build
```

---

## 3. Servicios disponibles

### FastAPI Swagger

Swagger:
http://localhost:8000/docs

### RabbitMQ Management

http://localhost:15672

Usuario:
guest

Password:
guest

# Flujo del sistema

1. Usuario crea pedido vía REST
2. Pedidos llama a Inventario vía gRPC
3. Inventario reserva stock
4. Pedidos publica evento en RabbitMQ
5. Notificaciones consume evento y envía email
6. Se simula el envío de email de confirmación.

---


