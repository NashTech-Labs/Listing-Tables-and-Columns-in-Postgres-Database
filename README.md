# PostgresDB Schema Explorer

This script allows you to explore the schema of a PostgresDB database. It connects to a PostgresDB  instance using psycopg2 and retrieves information about databases, collections, and fields (columns) within each collection.

## Prerequisites

Before running the script, make sure you have the following:

- Python installed on your system (Python 3 recommended)
- psycopg2 library installed (`pip install psycopg2`)

## Usage

1. **Configuration**: Open the script `table.py` in a text editor and provide the necessary PostgresDB connection information:

    ```python
    # PostgresDB connection information
    host = ''        # Replace with your PostgresDB  host
    port =           # Replace with your PostgresDB port
    username = ''    # Replace with your PostgresDB username
    password = ''    # Replace with your PostgresDB password
    ```

2. **Running the Script**: To run the script, execute the following command in your terminal or command prompt:

    ```bash
    python <file-name>
    ```

    This will connect to the specified PostgresDB instance, retrieve the schema information, and display it in the console.
