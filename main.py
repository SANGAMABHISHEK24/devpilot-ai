from fastapi import FastAPI

app = FastAPI(
    title="DevPilot AI",
    description="An autonomous software engineering assistant (starter version).",
    version="0.1.0",
)

@app.get("/")
def root():
    return {
        "name": "DevPilot AI",
        "status": "starter",
        "message": "Welcome to DevPilot AI.",
    }

@app.get("/health")
def health():
    return {"status": "ok"}
