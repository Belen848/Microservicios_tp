import pika


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()

channel.queue_declare(queue='order_confirmed')

mensaje = "Pedido #123 confirmado"

channel.basic_publish(
    exchange='',
    routing_key='order_confirmed',
    body=mensaje
)

print("Evento enviado correctamente")

connection.close()