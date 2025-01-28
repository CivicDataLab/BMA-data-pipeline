# cli.py
import typer
import subprocess
import os

app = typer.Typer()


@app.command()
def start(port: int = typer.Option(8080, "--port", "-p", help="Port to run server on")):
    """
    Start the Django development server
    """
    try:
        subprocess.run(["python", "manage.py", "runserver",
                       f"127.0.0.1:{port}"], check=True)
    except subprocess.CalledProcessError as e:
        typer.echo(f"Error starting server: {e}")
        raise typer.Exit(code=1)
    except KeyboardInterrupt:
        typer.echo("Server stopped")


@app.command()
def migrate():
    """
    Run Django migrations
    """
    try:
        subprocess.run(["python", "manage.py", "migrate"], check=True)
    except subprocess.CalledProcessError as e:
        typer.echo(f"Error running migrations: {e}")
        raise typer.Exit(code=1)


@app.command()
def shell():
    """
    Open Django shell
    """
    try:
        subprocess.run(["python", "manage.py", "shell"], check=True)
    except subprocess.CalledProcessError as e:
        typer.echo(f"Error opening shell: {e}")
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
