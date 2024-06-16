from decouple import config
import mysql.connector

database = mysql.connector.connect(
    host=config("DATABASE_HOST"),
    user=config("DATABASE_USER"),
    passwd=config("DATABASE_PASSWORD"),
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("All done!")

# cursorObject.close()
# database.close()
