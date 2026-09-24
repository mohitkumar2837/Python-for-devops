from fastapi import FastAPI
from bucket import get_buckets

app = FastAPI()


@app.get("/buckets")
def get_bucket():
    return get_buckets()