from invoke import task
from pathlib import Path
import platform
import json


REPO_ROOT = Path(__file__).parent
OS = platform.system().lower()
VENV_DIRNAME = Path('.venv')
PATHONPATHS = {
    'windows': VENV_DIRNAME / 'Scripts' / 'python.exe',
    'linux': VENV_DIRNAME / 'bin' / 'python',
    'darwin': VENV_DIRNAME / 'bin' / 'python',
}
VSCODE_SETTINGS = {
    "python.pythonPath": str(PATHONPATHS[OS]),
    "python.linting.enabled": True,
    "python.linting.pylintEnabled": False,
    "python.linting.flake8Enabled": True,
    "python.linting.flake8Args": ["--max-line-length=160"],
    "python.formatting.provider": "autopep8",
    "python.formatting.autopep8Args": ["--max-line-length=160"]
}


# VSCode

@task
def vscode(c):
    s = json.dumps(VSCODE_SETTINGS, indent=4)
    with open(REPO_ROOT / '.vscode' / 'settings.json', 'w', encoding='utf-8') as f:
        f.write(s)
    print('Done!')


# Django

@task
def migrate(c, docs=False):
    commands = [
        f'{PATHONPATHS[OS]} {REPO_ROOT / "onefake" / "manage.py"} makemigrations',
        f'{PATHONPATHS[OS]} {REPO_ROOT / "onefake" / "manage.py"} migrate',
        f'{PATHONPATHS[OS]} {REPO_ROOT / "twofake" / "manage.py"} makemigrations',
        f'{PATHONPATHS[OS]} {REPO_ROOT / "twofake" / "manage.py"} migrate',
        f'{PATHONPATHS[OS]} {REPO_ROOT / "lotterydraw" / "manage.py"} makemigrations',
        f'{PATHONPATHS[OS]} {REPO_ROOT / "lotterydraw" / "manage.py"} migrate',
    ]
    for command in commands:
        c.run(command)
    print('Done!')


@task
def createdata(c, docs=False):
    commands = [
        f'{PATHONPATHS[OS]} {REPO_ROOT / "onefake" / "manage.py"} createlottery',
        f'{PATHONPATHS[OS]} {REPO_ROOT / "twofake" / "manage.py"} createlottery',
        f'{PATHONPATHS[OS]} {REPO_ROOT / "lotterydraw" / "manage.py"} createlottery',
    ]
    for command in commands:
        c.run(command)
    print('Done!')


@task
def deletedata(c, docs=False):
    commands = [
        f'{PATHONPATHS[OS]} {REPO_ROOT / "onefake" / "manage.py"} deletelottery',
        f'{PATHONPATHS[OS]} {REPO_ROOT / "twofake" / "manage.py"} deletelottery',
        f'{PATHONPATHS[OS]} {REPO_ROOT / "lotterydraw" / "manage.py"} deletelottery',
    ]
    for command in commands:
        c.run(command)
    print('Done!')


@task
def runserver(c, docs=False):
    commands = [
        f'{PATHONPATHS[OS]} {REPO_ROOT / "onefake" / "manage.py"} runserver 8001',
        f'{PATHONPATHS[OS]} {REPO_ROOT / "twofake" / "manage.py"} runserver 8002',
        f'{PATHONPATHS[OS]} {REPO_ROOT / "lotterydraw" / "manage.py"} runserver 8000',
    ]
    merged_sign = ' && ' if OS == 'windows' else ' & '
    merged_command = merged_sign.join(commands)
    c.run(merged_command)


@task
def updatedata(c, docs=False):
    commands = [
        f'{PATHONPATHS[OS]} {REPO_ROOT / "onefake" / "manage.py"} updatelottery',
        f'{PATHONPATHS[OS]} {REPO_ROOT / "twofake" / "manage.py"} updatelottery',
        f'{PATHONPATHS[OS]} {REPO_ROOT / "lotterydraw" / "manage.py"} updatelottery',
    ]
    for command in commands:
        c.run(command)
    print('Done!')
