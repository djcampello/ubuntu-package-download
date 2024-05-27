"""Console script for ubuntu_package_download."""
import ubuntu_package_download

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for ubuntu_package_download."""
    console.print("Replace this message by putting your code into "
               "ubuntu_package_download.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
