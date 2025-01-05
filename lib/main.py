import jpype
import jpype.imports
from jpype.types import *

# Path to your .jar file
JAR_FILE = "lib/sqlite-jdbc-3.47.1.0.jar"  # Adjust this path to match where your .jar file is

# Path to your SQLite database file
DATABASE_PATH = "C:/Users/Niel/Desktop/Balos/db.sqlite3"  # Replace with the path to your SQLite database

# Start the JVM
jpype.startJVM(classpath=[JAR_FILE])

# Import Java classes
from java.sql import DriverManager, SQLException

try:
    # JDBC URL for SQLite
    jdbc_url = f"jdbc:sqlite:{DATABASE_PATH}"

    # Connect to the SQLite database
    connection = DriverManager.getConnection(jdbc_url)
    print("Connection successful!")

    # Example: Execute a query
    statement = connection.createStatement()
    result_set = statement.executeQuery("SELECT sqlite_version();")

    while result_set.next():
        print(f"SQLite version: {result_set.getString(1)}")

    # Close the connection
    connection.close()

except SQLException as e:
    print(f"SQL Exception: {e}")

finally:
    # Shutdown the JVM
    jpype.shutdownJVM()