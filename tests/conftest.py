import shutil
import pytest
from pathlib import Path
from fastapi.testclient import TestClient
from app.main import app
from app.config import PROJECT_DIR, BUILD_DIR


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def clean_workspace():
    for f in PROJECT_DIR.glob("*"):
        f.unlink()

    for f in BUILD_DIR.glob("*"):
        f.unlink()

    yield

    for f in PROJECT_DIR.glob("*"):
        f.unlink()

    for f in BUILD_DIR.glob("*"):
        f.unlink()