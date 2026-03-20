import subprocess
import shutil
from pathlib import Path
from app.config import PROJECT_DIR, BUILD_DIR, DEFAULT_CODE, RUNTIME_DIR


def list_files():
    return [f.name for f in PROJECT_DIR.glob("*.cs")]


def create_file(filename: str):

    if not filename.endswith(".cs"):
        filename += ".cs"

    path = PROJECT_DIR / filename
    with open(path, "w") as f:
        f.write(DEFAULT_CODE)

    return filename


def read_file(filename: str):
    path = PROJECT_DIR / filename
    return path.read_text()


def edit_file(filename: str, content: str):

    path = PROJECT_DIR / filename
    path.write_text(content)

    return True


def delete_file(filename: str):

    path = PROJECT_DIR / filename

    if path.exists():
        path.unlink()

    return True


def build_file(filename: str):

    src = PROJECT_DIR / filename

    if not src.exists():
        return "Source file not found"

    BUILD_DIR.mkdir(parents=True, exist_ok=True)

    try:
        result = subprocess.run(
            ["python3", "compiler/run.py", str(src)],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            return result.stdout or result.stderr

        for f in RUNTIME_DIR.glob("*.class"):
            shutil.copy(f, BUILD_DIR / f.name)

        return result.stdout

    except Exception as e:
        return f"Build failed: {e}"


def run_file():

    main_class = BUILD_DIR / "CS.class"

    if not main_class.exists():
        return "Build file not found"

    try:
        result = subprocess.run(
            ["java", "-cp", str(BUILD_DIR), "CS"],
            capture_output=True,
            text=True
        )

        return result.stdout

    except Exception as e:
        return f"Run error: {e}"