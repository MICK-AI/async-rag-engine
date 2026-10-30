from redis import Redis
from rq import Queue, SimpleWorker

redis_conn = Redis(
    host="localhost",
    port=6379,
    db=0
)

queue = Queue("default", connection=redis_conn)

if __name__ == "__main__":
    print("Starting Windows-compatible RQ worker...")

    worker = SimpleWorker(
        [queue],
        connection=redis_conn
    )

    print("Worker type:", type(worker).__name__)

    worker.work()