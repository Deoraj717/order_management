from fastapi import fastapi

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status":"ok"}

