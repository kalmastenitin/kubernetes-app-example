from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from api import static_dir
import os

router = APIRouter()


@router.get("/hello")
def greet_hello():
    return {"msg": "welcome"}


@router.put("/upload_file")
def add_file_to_project(file: UploadFile = File(...)):
    ''' upload only image files here '''
    try:
        file_name = f'{static_dir}/{file.filename}'
        with open(file_name, "wb", buffering=0) as buffer:
            contents = file.file.read()
            buffer.write(contents)
        print(file_name)
        print(os.path.exists(file_name))
        return JSONResponse({"message": "success"}, status_code=200)
    except Exception as e:
        return JSONResponse({"message": str(e)}, status_code=500)
