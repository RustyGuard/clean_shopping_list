import os

import typer

from src.clean_shopping_list.config import get_config
from src.clean_shopping_list.presentation.web_api.app import get_application

cli = typer.Typer()
app = get_application()


@cli.command()
def serve(workers: int = 1):
    config = get_config()
    os.system(f'gunicorn manage:app --workers {workers} --worker-class uvicorn.workers.UvicornWorker '
              f'--bind {config.HOST}:{config.PORT}')


@cli.command()
def stub():
    pass


if __name__ == '__main__':
    cli()
