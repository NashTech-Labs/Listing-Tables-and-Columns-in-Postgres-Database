import psycopg2

def get_all_tables_and_columns(host, port, database, user, password):
    connection = None
    try:
        # Establish a connection to the PostgreSQL database
        connection = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )

        cursor = connection.cursor()

        # Fetch all database names
        cursor.execute("SELECT datname FROM pg_database WHERE datistemplate = false")
        databases = cursor.fetchall()

        all_tables_columns = {}
        # Iterate over each database
        for database in databases:
            database_name = database[0]
            print(f"Processing database: {database_name}")

            # Establish connection to the current database
            db_connection = psycopg2.connect(
                host=host,
                port=port,
                database=database_name,
                user=user,
                password=password
            )
            db_cursor = db_connection.cursor()

            # Fetch all table names
            db_cursor.execute("""
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public'
                ORDER BY table_name
            """)
            tables = db_cursor.fetchall()

            # Fetch columns for each table
            table_columns = {}
            for table in tables:
                table_name = table[0]
                db_cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}'")
                columns = db_cursor.fetchall()
                table_columns[table_name] = [column[0] for column in columns]

            all_tables_columns[database_name] = table_columns

            # Close cursor and connection for the current database
            db_cursor.close()
            db_connection.close()

        return all_tables_columns

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # Close main database connection
        if connection:
            cursor.close()
            connection.close()

# Replace these variables with your PostgreSQL connection details
host =        # Replace with your PostgreSQL host
port =            # Replace with your PostgreSQL port
database = # Replace with your PostgreSQL database name
user =           # Replace with your PostgreSQL username
password =  # Replace with your PostgreSQL password

all_tables_and_columns = get_all_tables_and_columns(host, port, database, user, password)
for database, tables_columns in all_tables_and_columns.items():
    print(f"Database: {database}")
    for table, columns in tables_columns.items():
        print(f"  Table: {table}")
        print("  Columns:")
        for column in columns:
            print(f"    - {column}")
    print()
