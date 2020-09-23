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
    file1 = BASE_DIR / '.vscode' / 'd4settings.json'
    file2 = BASE_DIR / '.vscode' / 'settings.json'
    shutil.copy(file1, file2)


@task
def createdata(c, docs=False):
    c.run(f'{PATHON_PATHS[OS]} {BASE_DIR / "onefake" / "manage.py"} makemigrations')
    c.run(f'{PATHON_PATHS[OS]} {BASE_DIR / "onefake" / "manage.py"} migrate')
    c.run(f'{PATHON_PATHS[OS]} {BASE_DIR / "onefake" / "manage.py"} createlottery')
    c.run(f'{PATHON_PATHS[OS]} {BASE_DIR / "twofake" / "manage.py"} makemigrations')
    c.run(f'{PATHON_PATHS[OS]} {BASE_DIR / "twofake" / "manage.py"} migrate')
    c.run(f'{PATHON_PATHS[OS]} {BASE_DIR / "twofake" / "manage.py"} createlottery')
    c.run(f'{PATHON_PATHS[OS]} {BASE_DIR / "lotterydraw" / "manage.py"} makemigrations')
    c.run(f'{PATHON_PATHS[OS]} {BASE_DIR / "lotterydraw" / "manage.py"} migrate')
    c.run(f'{PATHON_PATHS[OS]} {BASE_DIR / "lotterydraw" / "manage.py"} createlottery')


@task
def deletedata(c, docs=False):
    c.run(f'{PATHON_PATHS[OS]} {BASE_DIR / "onefake" / "manage.py"} makemigrations')
    c.run(f'{PATHON_PATHS[OS]} {BASE_DIR / "onefake" / "manage.py"} migrate')
    c.run(f'{PATHON_PATHS[OS]} {BASE_DIR / "onefake" / "manage.py"} deletelottery')
    c.run(f'{PATHON_PATHS[OS]} {BASE_DIR / "twofake" / "manage.py"} makemigrations')
    c.run(f'{PATHON_PATHS[OS]} {BASE_DIR / "twofake" / "manage.py"} migrate')
    c.run(f'{PATHON_PATHS[OS]} {BASE_DIR / "twofake" / "manage.py"} deletelottery')
    c.run(f'{PATHON_PATHS[OS]} {BASE_DIR / "lotterydraw" / "manage.py"} makemigrations')
    c.run(f'{PATHON_PATHS[OS]} {BASE_DIR / "lotterydraw" / "manage.py"} migrate')
    c.run(f'{PATHON_PATHS[OS]} {BASE_DIR / "lotterydraw" / "manage.py"} deletelottery')


@task
def demo(c, docs=False):
    c1 = f'{PATHON_PATHS[OS]} {BASE_DIR / "onefake" / "manage.py"} runserver 8001'
    c2 = f'{PATHON_PATHS[OS]} {BASE_DIR / "twofake" / "manage.py"} runserver 8002'
    c3 = f'{PATHON_PATHS[OS]} {BASE_DIR / "lotterydraw" / "manage.py"} runserver 8000'
    command = ' & '.join([c1, c2, c3])
    c.run(command)


@task
def updatedata(c, docs=False):
    c.run(f'{PATHON_PATHS[OS]} {BASE_DIR / "onefake" / "manage.py"} updatelottery')
    c.run(f'{PATHON_PATHS[OS]} {BASE_DIR / "twofake" / "manage.py"} updatelottery')
    c.run(f'{PATHON_PATHS[OS]} {BASE_DIR / "lotterydraw" / "manage.py"} updatelottery')
