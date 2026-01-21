from celery import Celery

celery_app = Celery(
    "crypto",
    broker="redis://localhost:6379/0",
)
