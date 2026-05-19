from dotenv import load_dotenv
load_dotenv()
import os
import sys
from fastapi import FastAPI


def require_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        print(f"ERROR: Required environment variable '{name}' is not set.")
        print("       Check your .env file or deployment configuration.")
        sys.exit(1)
    return value


APP_ENV = require_env("APP_ENV")
PORT = int(os.environ.get("PORT", "8000"))

print("Starting DevOps Lab API")
print(f"  APP_ENV: {APP_ENV}")
print(f"  PORT:    {PORT}")

app = FastAPI(title="DevOps Lab API", version="1.0.0")


@app.get("/")
def root():
    return {"message": "Welcome to the DevOps Lab", "status": "running"}


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "version": "1.0.0",
        "environment": APP_ENV
    }
