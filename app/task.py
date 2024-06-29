from celery import Celery

celery = Celery(
    "tasks",
    broker="amqp://rabbitmq:rabbitmq@rabbitmq:5672//",
    backend="db+postgresql://postgres:postgres@db:5432/celery",
)


@celery.task
def add(x, y):
    return x + y

# celery -A app.task worker --loglevel=info
