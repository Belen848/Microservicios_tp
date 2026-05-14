import pika
import time


while True:

    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='rabbitmq')
        )

        break

    except Exception:
        print("Esperando RabbitMQ...")
        time.sleep(5)


channel = connection.channel()

channel.queue_declare(queue='order_confirmed')


def callback(ch, method, properties, body):

    mensaje = body.decode()

    
    print(f"Email enviado -> {mensaje}", flush=True)

channel.basic_consume(
    queue='order_confirmed',
    on_message_callback=callback,
    auto_ack=True
)

print("Servicio Notificaciones esperando mensajes...")

channel.start_consuming()