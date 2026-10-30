from fastapi import FastAPI , Query
from client.rq_client import queue
from .worker import process_query
app = FastAPI()

@app.get('/')
def root():
    return {"status": 'server is up and running'}

@app.post('/')
def chat(query: str = Query(..., description="The chat query of user")):

    job = queue.enqueue(process_query, query)

    return {
        "message": "Query successfully queued",
        "job_id": job.id,
        "status": job.get_status()
    }

@app.get('/job-status')
def get_result(
        job_id: str = Query(...,description="Job ID")
    ):
    job = queue.fetch_job(job_id=job_id)
    result= job.return_value()
    return {"result": result}