from invoke import task
from pathlib import Path
import shutil


@task
def d4vscode(c):
    basedir = Path(__file__).parent
    file1 = basedir / '.vscode' / 'd4settings.json'
    file2 = basedir / '.vscode' / 'settings.json'
    shutil.copy(file1, file2)
