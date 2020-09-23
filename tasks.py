from invoke import task
from pathlib import Path
import platform
import shutil


OS = platform.system().lower()
BASE_DIR = Path(__file__).parent
PYTHON_VENV_DIR_NAME = '.venv'
PATHON_PATHS = {
    'windows': BASE_DIR / PYTHON_VENV_DIR_NAME / 'Scripts' / 'python.exe',
    'linux': BASE_DIR / PYTHON_VENV_DIR_NAME / 'bin' / 'python',
    'darwin': BASE_DIR / PYTHON_VENV_DIR_NAME / 'bin' / 'python',
}


@task
def d4vscode(c):
    basedir = Path(__file__).parent
    file1 = basedir / '.vscode' / 'd4settings.json'
    file2 = basedir / '.vscode' / 'settings.json'
    shutil.copy(file1, file2)


@task
def demo(c, docs=False):
    c.run(f'{PATHON_PATHS[OS]} {BASE_DIR / "lotterydraw" / "manage.py"} runserver')
