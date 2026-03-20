from fastapi import APIRouter
from app.schemas.file_schema import CreateFile, EditFile
from app.services import file_service

router = APIRouter(prefix="/files")


@router.get("/")
def list_files():
    return file_service.list_files()

@router.post("/create")
def create_file(data: CreateFile):
    return file_service.create_file(data.filename)

@router.get("/run")
def run_file():
    return file_service.run_file()

@router.get("/{filename}")
def read_file(filename: str):
    return file_service.read_file(filename)


@router.post("/edit/{filename}")
def edit_file(filename: str, data: EditFile):
    return file_service.edit_file(filename, data.content)

@router.delete("/{filename}")
def delete_file(filename: str):
    return file_service.delete_file(filename)


@router.post("/build/{filename}")
def build_file(filename: str):
    return file_service.build_file(filename)


