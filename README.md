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

The included data (`titanic.csv`) is from the following reference; [https://github.com/datasciencedojo/datasets/blob/master/titanic.csv](https://github.com/datasciencedojo/datasets/blob/master/titanic.csv).

## Output

We display the csv file and leave the exploration of data to the user. 

Sample output
``` 
...
880,1,1,"Potter, Mrs. Thomas Jr (Lily Alexenia Wilson)",female,56,0,1,11767,83.1583,C50,C
881,1,2,"Shelley, Mrs. William (Imanita Parrish Hall)",female,25,0,1,230433,26,,S
882,0,3,"Markun, Mr. Johann",male,33,0,0,349257,7.8958,,S
883,0,3,"Dahlberg, Miss. Gerda Ulrika",female,22,0,0,7552,10.5167,,S
884,0,2,"Banfield, Mr. Frederick James",male,28,0,0,C.A./SOTON 34068,10.5,,S
885,0,3,"Sutehall, Mr. Henry Jr",male,25,0,0,SOTON/OQ 392076,7.05,,S
886,0,3,"Rice, Mrs. William (Margaret Norton)",female,39,0,5,382652,29.125,,Q
887,0,2,"Montvila, Rev. Juozas",male,27,0,0,211536,13,,S
888,1,1,"Graham, Miss. Margaret Edith",female,19,0,0,112053,30,B42,S
889,0,3,"Johnston, Miss. Catherine Helen ""Carrie""",female,,1,2,W./C. 6607,23.45,,S
890,1,1,"Behr, Mr. Karl Howell",male,26,0,0,111369,30,C148,C
891,0,3,"Dooley, Mr. Patrick",male,32,0,0,370376,7.75,,Q
```

Now, what do you want to do with this data?!
