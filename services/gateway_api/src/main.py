from fastapi import FastAPI
from .api.routers import health, projects, topics, runs, assets, publish, commands, queries

app = FastAPI(title="Publishr Gateway API")
for router in [health.router, projects.router, topics.router, runs.router, assets.router, publish.router, commands.router, queries.router]:
    app.include_router(router)
