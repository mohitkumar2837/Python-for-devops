from fastapi import FastAPI, UploadFile, File
from bucket import upload_file

app = FastAPI()


@app.post("/upload/{bucket_name}")
async def upload_to_s3(
    bucket_name: str,
    file: UploadFile = File("python-for-devops/day-01/upload-file-s3/file.txt")
):
    return upload_file(
        file.file,
        bucket_name,
        file.filename
    )