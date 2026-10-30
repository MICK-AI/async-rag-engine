# Async RAG Engine 🚀

An asynchronous Retrieval-Augmented Generation (RAG) system built using **FastAPI, Redis Queue (RQ), Qdrant, Hugging Face Sentence Transformers, and Gemini API**.

The project uses background job processing to handle RAG queries asynchronously, allowing the API to enqueue requests and retrieve their results using job IDs.

## 🏗️ Architecture

```text
             User Query
                 |
                 v
             FastAPI
                 |
                 v
           Redis Queue (RQ)
                 |
                 v
             RQ Worker
                 |
          +------+------+
          |             |
          v             v
       Qdrant        Gemini API
    Vector Search    Response
          |             |
          +------+------+
                 |
                 v
           Generated Answer
                 |
                 v
          Job Status API
```

## ⚙️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | API development |
| Redis | Message broker and job queue |
| RQ | Background job processing |
| Qdrant | Vector database |
| Hugging Face | Text embeddings |
| Sentence Transformers | Embedding model |
| Gemini API | LLM response generation |
| Docker Compose | Service management |

## ✨ Features

- Asynchronous RAG query processing.
- Background task execution using Redis Queue.
- Job ID generation and status tracking.
- Semantic document retrieval using Qdrant.
- Context-aware response generation using Gemini.
- Sentence embeddings using `all-MiniLM-L6-v2`.
- Modular project structure separating API, queue configuration, and worker logic.

## 📁 Project Structure

```text
async-rag-engine/
│
├── client/
│   ├── __init__.py
│   └── rq_client.py
│
├── queues/
│   ├── __init__.py
│   ├── main.py
│   ├── server.py
│   ├── run_worker.py
│   └── worker.py
│
├── .env.example
├── .gitignore
├── docker-compose.yml
└── README.md
```

## 🛠️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/MICK-AI/async-rag-engine.git

cd async-rag-engine
```

### 2. Create a virtual environment

```bash
python -m venv ragenv
```

Activate it on Windows:

```powershell
.\ragenv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root using `.env.example` as a template.

```env
GEMINI_API_KEY=your_gemini_api_key
```

Never commit your actual API keys or `.env` file.

### 5. Start Redis and Qdrant

If using the provided Docker Compose configuration:

```bash
docker compose up -d
```

Ensure Redis and Qdrant are accessible at:

- Redis: `localhost:6379`
- Qdrant: `localhost:6333`

### 6. Start the FastAPI server

```bash
python -m queues.main
```

API documentation:

```text
http://localhost:8000/docs
```

### 7. Start the RQ worker

Open another terminal in the project directory:

```bash
python -m queues.run_worker
```

The worker listens for queued jobs and executes the RAG processing function.

**Note:** This project currently uses `SimpleWorker` for local development on Windows. It executes jobs in the worker process without the process-forking behavior of the default RQ Worker.

## 🔄 How It Works

1. A user submits a query through the FastAPI endpoint.
2. FastAPI adds the query as a background job to Redis Queue.
3. Redis assigns the job to the available RQ worker.
4. The worker retrieves relevant document chunks from Qdrant.
5. Retrieved context is passed to the Gemini API.
6. Gemini generates a context-aware response.
7. The result is stored against the job ID and can be retrieved through the status endpoint.

## 🔐 Environment Variables

| Variable | Description |
|---|---|
| `GEMINI_API_KEY` | Gemini API authentication key |

## 🚧 Future Improvements

- Retry mechanisms and better failure handling.
- Document ingestion and indexing pipeline.
- Improved logging and monitoring.
- Worker concurrency and performance testing.
- Dockerized application deployment.
- Authentication and API rate limiting.

## 👨‍💻 Author

**MICK-AI**

- GitHub: [MICK-AI](https://github.com/MICK-AI)
- Portfolio: [mickverse.in](https://mickverse.in)

---

*Built as a hands-on project to explore asynchronous processing, vector databases, and scalable RAG system architecture.*