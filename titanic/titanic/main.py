#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rich.console import Console
import typer
from pathlib import Path

# create a Typer object to support the command-line interface

cli = typer.Typer()

console = Console()

@cli.command()
def main(
    data_file: Path = typer.Option(...),
):
    """Summarize the data values stored in a file."""
    # display details about the file provided on the command line
    data_text = ""
    # --> the file was not specified so we cannot continue using program
    if data_file is None:
        console.print("No data file specified!")
        raise typer.Abort()
    # --> the file was specified and it is valid so we should read and check it
    if data_file.is_file():
        data_text = data_file.read_text()
        data_line_count = len(data_text.splitlines())
        console.print(
            f":microscope: The data file contains {data_line_count} data values in it! Let's get summarizing!"
        )
        console.print()
        console.print(f"data_text : {data_text} ")
        console.print("Now, what do you want to do with this data?!")
    # --> the file was specified but it does not exist so we cannot continue using program
    elif not data_file.exists():
        console.print("The data file does not exist!")


# @cli.command()
# def old_main(first: str = "", middle: str = "", last: str = ""):
#     """Say hello to the person having a name
#     of first, middle and last name"""
#     console = Console()
#     console.print("Hello to;")
#     console.print(f"first = {first}")
#     console.print(f"middle = {middle}")
#     console.print(f"last = {last}")


# # end of main()
