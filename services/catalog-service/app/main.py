from fastapi import FastAPI

app = FastAPI(title="Catalog Service", version="0.1.0")


@app.get("/")
def root():
    return {"service": "catalog-service", "status": "ok"}


@app.get("/health")
def health():
    return {"status": "ok", "service": "catalog-service"}