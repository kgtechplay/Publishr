# Publishr Setup Guide

## Prerequisites
- Python 3.11+
- Docker + Docker Compose
- GNU Make (optional)

## 1) Start infrastructure
```bash
docker compose -f docker-compose.dev.yml up -d
```

## 2) Configure environment
```bash
cp .env.example .env
```
Update keys as needed.

## 3) Install dependencies
```bash
make setup
```

## 4) Run API
```bash
make run-gateway
```

## 5) Health check
```bash
curl http://localhost:8000/health
```

## Worker startup (example)
Run each worker in separate terminals:
```bash
python services/worker_research/src/worker.py
python services/worker_draft/src/worker.py
python services/worker_generate/src/worker.py
python services/worker_publish/src/worker.py
```

## Migrations
Use the migration folder in `infra/migrations` with Alembic.
