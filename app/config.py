from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

WORKSPACE = BASE_DIR / "workspace"
PROJECT_DIR = WORKSPACE / "projects"
BUILD_DIR = BASE_DIR / "build"
RUNTIME_DIR = BASE_DIR / "compiler/src/runtime"

PROJECT_DIR.mkdir(parents=True, exist_ok=True)
BUILD_DIR.mkdir(parents=True, exist_ok=True)

DEFAULT_CODE = """
// ------------ Program --------------
const  a = 2;
const b = 3 + a;
print(a + b);
// ------------------------------------
"""