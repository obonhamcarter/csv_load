# csv_load
Demo of how to open CSV files in Poetry

24 April 2024
Oliver Bonaham-Carter

## Poetry Framing

The code requires [Poetry](https://python-poetry.org/docs/) for execution.

## Commands

+ Set up project

    ``` bash
    poetry install
    ```

+ Get help

    ``` bash
    poetry run titanic --help 
    ```

+ Run program to load a csv file (`input/titanic.csv`)
    ``` bash
    poetry run titanic --data-file input/titanic.csv
    ```

## Data

The included data (`tatanic.csv`) is from the following reference; [https://github.com/datasciencedojo/datasets/blob/master/titanic.csv](https://github.com/datasciencedojo/datasets/blob/master/titanic.csv).