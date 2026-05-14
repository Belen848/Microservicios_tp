# MPI Microservicios - Sistemas Distribuidos

Como objetivo se  propone migrar un monolito hacia una arquitectura de microservicios utilizando:

- FastAPI
- gRPC
- RabbitMQ
- Docker

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
mpi-microservicios/
├── inventario/
├── pedidos/
├── notificaciones/
└── README.md
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

## 2. Crear entorno virtual

```bash
python -m venv venv
```

Activar entorno:

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Instalar dependencias

### Inventario

```bash
cd inventario
pip install -r requirements.txt
```

### Pedidos

```bash
cd ../pedidos
pip install -r requirements.txt
```

### Notificaciones

```bash
cd ../notificaciones
pip install -r requirements.txt
```

---

# Levantar RabbitMQ

```bash
docker run -d --hostname rabbitmq --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

Panel web:

http://localhost:15672

Usuario:
guest

Password:
guest

---

# Ejecución

## 1. Levantar Inventario

```bash
cd inventario
python server.py
```

Servidor gRPC:
localhost:50051

---

## 2. Levantar Notificaciones

```bash
cd notificaciones
python worker.py
```

---

## 3. Levantar Pedidos

```bash
cd pedidos
uvicorn main:app --reload
```

Swagger:
http://localhost:8000/docs

---

# Flujo del sistema

1. Usuario crea pedido vía REST
2. Pedidos llama a Inventario vía gRPC
3. Inventario reserva stock
4. Pedidos publica evento en RabbitMQ
5. Notificaciones consume evento y envía email

---


